#! /usr/bin/bash
#This script is used to build the casadocs repository https://github.com/casangi/casadocs

# runcmd doesn't expand "~" in paths
h=$( \cd ~; pwd )
cwd=$( pwd )
docsdir=$( pwd )
realdocsdir=$( realpath "$docsdir" )

usage="$0 --help
$0 --sphinx [--installpypkgs] [--copyxml devdir]"
help="Usage:
$usage

Builds the documentation webpages for casadocs.

--sphinx         Run sphinx-build to generate webpages.
--copyxml        Copy the xml from the source development directory INSTEAD OF cloning the branch fresh.
                 For example, with devdir \"~/dev/CAS-6692\", this will copy the contents:
                 \"~/dev/CAS-6692/src/casa6/casatools/xml/*.xml\" and \"~/dev/CAS-6692/src/casa6/casatasks/xml/*.xml\"
--tools          List of tools to include, separated by commas. All other tools will be excluded. 'none' for no tools. Eg:
                 --tools logsink,regionmanager
--tasks          Like tools, but for tasks. Must include the category of the task name. Eg:
                 --tasks analysis.imfit,imaging.tclean
--notebooks      Like tools, but for notebooks. Eg:
                 --notebooks image_visualization
--nobel          Don't 'tput bel' at the end of a successful execution.
--installpypkgs  Installs any missing python pip packages.
"

#############################################################################################################
##
## Parse input options
##
#############################################################################################################

sphinx=0
installpypkgs=0
copyxml=0
copyxmldevdir=""
tools=0
toolsnames=""
tasks=0
tasksnames=""
notebooks=0
notebooksnames=""
tmpnobel=""
while test $# -gt 0
do
    _ARG="$1"
    _ARG2=""
    if [ "$#" -gt 1 ]; then
        _ARG2="$2"
    fi

    case "$_ARG" in
        --help) echo "$help"
            exit 0
            ;;
        --sphinx) sphinx=1
            ;;
        --installpypkgs) installpypkgs=1
            ;;
        --copyxml) copyxml=1
            if [ "$#" -gt 1 ] && [[ ! $_ARG2 == -* ]]; then
                tmpdevdir="$_ARG2"
                echo "$tmpdevdir"
                tmpdevdir=$( \cd "$tmpdevdir"; pwd )
                echo "$tmpdevdir"
                copyxmldevdir=$( realpath "$tmpdevdir" )
                echo "$copyxmldevdir"
                shift
            else
                echo "Missing dirname after argument $_ARG"
                echo "$usage"
                exit 1
            fi
            ;;
        --tools) tools=1
            if [ "$#" -gt 1 ] && [[ ! $_ARG2 == -* ]]; then
                toolsnames="$_ARG2"
                shift
            else
                echo "Missing tools names after argument $_ARG"
                echo "$usage"
                exit 1
            fi
            ;;
        --tasks) tasks=1
            if [ "$#" -gt 1 ] && [[ ! $_ARG2 == -* ]]; then
                tasksnames="$_ARG2"
                shift
            else
                echo "Missing tasks names after argument $_ARG"
                echo "$usage"
                exit 1
            fi
            ;;
        --notebooks) notebooks=1
            if [ "$#" -gt 1 ] && [[ ! $_ARG2 == -* ]]; then
                notebooksnames="$_ARG2"
                shift
            else
                echo "Missing notebooks names after argument $_ARG"
                echo "$usage"
                exit 1
            fi
            ;;
        --nobel) nobel=$_ARG
            tmpnobel="$nobel"
            ;;
        --*) echo ""
            echo "----------------- bad option $_ARG -----------------"
            echo ""
            exit 1
            ;;
        *) echo ""
            echo "----------------- bad argument $_ARG -----------------"
            echo ""
            exit 1
            ;;
    esac
    shift
done

#############################################################################################################
##
## Setup
##
#############################################################################################################

# Checks that the return value passed in is 0. Otherwise exits with that return value.
function retcheck {
    ret="$1"
    if [ $ret -ne 0 ]; then
        if [ "$#" -gt 1 ]; then
            echo "Command failed: $2"
        fi
        exit $ret
    fi
}

# Executes the command passed in and calls retcheck afterwards.
function runcmd {
    cmd="$1"
    shift
    while test $# -gt 0
    do
        cmd="$cmd $1"
        shift
    done

    echo "$cmd"
    eval "$cmd"
    retcheck $? "$cmd"
}

# activate the python venv to use the local copy of pip and python
source $realdocsdir/venv/bin/activate; retcheck $? "Failed to activate venv. Try running \"python3 -m venv ${docsdir}/venv\""

if [[ "$installpypkgs" == "1" ]]; then
    runcmd "pip install --upgrade pip wheel"
    runcmd "pip install -r requirements.txt"
else
    # sanity check
    echo "pip check requirements.txt"; eval "pip check requirements.txt"; success=$?
    if [[ "$success" != "0" ]]; then
        echo ""
        echo "Failed to verify python package requirements."
        echo "Try running this first:"
        echo "$0 --installpypkgs"
        echo ""
    fi
fi

if [[ "$copyxml" == "1" ]]; then
    if [[ ! -e "$copyxmldevdir/src/casa6/casatools/xml" ]] || [[ ! -e "$copyxmldevdir/src/casa6/casatasks/xml/" ]]; then
        echo "Can't find one or more of the xml directories: $copyxmldevdir/src/casa6/casatools/xml, $copyxmldevdir/src/casa6/casatasks/xml/"
        echo "$usage"
        exit 1
    fi
    
    # this copy option is intended to be used in place of downloading data
    runcmd "cd $realdocsdir/scripts"
    runcmd "git checkout -- download_xml.py"
    contents=$( cat download_xml.py )
    echo "raise RuntimeError('Dont download data right now')
${contents}" > download_xml.py
    retcheck $? "skip downloads"
    echo "skip downloads"

    # copy the xml values
    runcmd "cd $copyxmldevdir"
    runcmd "cp -p src/casa6/casatools/xml/*.xml $realdocsdir/casasource/casa6/casatools/xml/"
    runcmd "cp -p src/casa6/casatasks/xml/*.xml $realdocsdir/casasource/casa6/casatasks/xml/"
else
    runcmd "cd $realdocsdir/scripts"
    runcmd "git checkout -- download_xml.py"
fi

# include only specified files
runcmd "cd $realdocsdir"
rm docs/tools_selection.csv
rm docs/tasks_selection.csv
rm docs/notebooks_selection.csv
if [[ "$tools" == "1" ]]; then
    runcmd "echo '${toolsnames}' > docs/tools_selection.csv"
fi
if [[ "$tasks" == "1" ]]; then
    runcmd "echo '${tasksnames}' > docs/tasks_selection.csv"
fi
if [[ "$notebooks" == "1" ]]; then
    runcmd "echo '${notebooksnames}' > docs/notebooks_selection.csv"
fi

#############################################################################################################
##
## Build casadocs
##
#############################################################################################################
if [[ "$sphinx" == "1" ]]; then
    runcmd "cd $realdocsdir/docs"
    runcmd "sphinx-build -a -E -b html . ./build"
    runcmd "cd ../"
    echo "Try opening this in your favorite web browser:"
    echo "${cwd}/docs/build/index.html"
fi

if [[ "$copyxml" == "1" ]]; then
    runcmd "cd $realdocsdir/scripts"
    runcmd "git checkout -- download_xml.py"
fi

if [[ $tmpnobel == "" ]]; then tput bel; fi
deactivate