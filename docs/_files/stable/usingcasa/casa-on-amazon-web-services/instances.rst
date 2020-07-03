.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Instances
=========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   An instance is effectively a single computer composed of an OS,
   processors, memory, base storage and optional additional data storage

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Instance Types
         :name: instance-types

      Amazon has predefined over 40 instance types. These fall into
      classes defined roughly by processing power, which are further
      subdivided by total memory and base storage.

      `Click here to see a list of all Linux instance types with their
      number of  virtual CPUs (vCPU), total memory in GBytes of RAM, and
      the type of storage utilized by the instance
      type. <https://aws.amazon.com/ec2/pricing>`__

      Note the "vCPU" is actually a hyperthread, so 2 "vCPU" equal one
      core, e.g. m4.xlarge has 2 cores. (These prices are for on-demand
      instances.)

      .. rubric:: Starting Instances
         :name: starting-instances

      CASA requires >=4GB/core. Storage can be EBS. Because AWS has
      hyperthreading turned on, each "vCPU" is one hyperthread and
      therefore 2 vCPUs essentially equal 1 physical core. Some
      experimentation may be required to optimize the instance type if
      many instances are to be used. This can have a very significant
      impact on total run time and cost. The 4GB per physical core rule
      should be sufficient to get started.

      .. rubric:: Choosing a Payment Option: On-demand vs. Spot
         :name: choosing-a-payment-option-on-demand-vs.-spot

      Choosing an on-demand instance (the default) guarantees you the
      use of that instance (barring hardware failure).

      There is also a Spot Price market; `click here to read about
      it <https://aws.amazon.com/ec2/spot/pricing/>`__. The price of an
      instance fluctuates over time as a function of demand.  AWS fills
      spot requests starting at the highest bid and working down to the
      lowest, the bid price paid by all spot users is the bid price
      reached when all resources were exhausted.  When you request a
      spot instance you submit a bid for those resources.  If that bid
      exceeds the current spot price, then the spot instance will launch
      and continue to run as long as the spot price remains below the
      bid. Typically, the spot price is much less than the on-demand
      price, so bidding the on-demand price typically permits an
      instance to run its job to completion. During the time it runs, it
      is billed only at the running spot price, not the bid, so the
      savings can be considerable.  If the spot price rises above your
      bid your instance will be terminated.  Be warned, if demand is
      excessive for that particular instance type and you bid 2x or more
      of the on-demand price you run the risk of the spot price rising
      to that level.  Over bidding the demand price is most useful for
      very long running jobs where it's considered acceptable to pay
      more for brief periods while minimizing the risk that the instance
      will be terminated due to a low bid.

      For example, the on-demand price for a m4.xlarge instance is
      $0.239 per hour. For the past 3 months, the mean spot price has
      been $0.0341 (maximum $0.0515 per hour). A 10-hour run of 100
      instances would have cost $239 for on-demand and $34 for spot
      instances. That assumes adding 100 instances to the spot market
      will not affect the spot price much, which is a reasonable
      assumption. However, adding 500 instances will certainly raise the
      spot price.

      It's possible to bid up to 10 times the on-demand price.

      There are other ways to purchase AWS instances, but only on-demand
      and spot instances appear of interest to running CASA. `See
      purchasing
      options. <https://aws.amazon.com/ec2/purchasing-options/>`__

.. container:: section
   :name: viewlet-below-content-body
