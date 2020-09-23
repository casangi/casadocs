# casadocs
Common Astronomy Software Applications Documentation


## Updating
The generated documentation is held in either Jupyter notebook .ipynb format 
or RestructuredText .rst format.  Jupyter notebook pages have a link at the 
to "Open in Colab" for editing.  RestructuredText files can be edited in the
Github browser window.


## Generating from Scratch

1. Scrape the latest Plone CASAdocs (creates html folder):
   ```
   $: scrapy crawl sitemap
   $: docker run -p 8050:8050 scrapinghub/splash
   $: scrapy crawl full
   ```

2. Generate content pages (creates markdown folder)
   ```
   $: python scripts/convert_html.py
   ``` 

3. Generate notebook files (creates docs/notebooks folder)
   ```
   $: python scripts/build_notebooks.py
   ```

4. Generate API files (creates stubs folder)
   ```
   $: python scripts/parse_tasks.py
   ```

5. Locally build pages to verify
   ```
   $: cd docs
   $: sphinx-build -a -E -b html . ./build
   ```


.. TODO:
1. Add horizontal TOC to top of task pages - DONE
2. pull release notes to a change history section for each task
3. start using release branches instead of tags
4. look at jira link to casadocs branches
5. disable task categories and/or add global index - DONE 


