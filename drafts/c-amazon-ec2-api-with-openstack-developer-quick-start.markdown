Title: Amazon EC2 API with OpenStack - Developer Quick Start
Date: 2014-04-24
Author: Rushi Agrawal
Summary: 
Tags: 
Category: 

OpenStack has support for EC2 API, that is, you can fire Amazon's API against an OpenStack cloud and it will still work. This article just gets one started with using them locally against DevStack. It is more of a starter guide to a novice here.

Install and import boto

	sudo apt-get install python-pip
	sudo pip install boto

Fire a DevStack with it's default settings. See [this post](www.rushiagr.com/blog/2014/04/03/openstack-in-an-hour-with-devstack) for more information on it.

	git clone http://github.com/openstack-dev/devstack
	cd devstack/
	./stack.sh

Source openrc

	source openrc

View all EC2 credentials available for the current user (here, `demo` user in `demo` tenant)

	$ keystone ec2-credentials-list 
	+----------------------------------+----------------------------------+----------------------------------+
	|              tenant              |              access              |              secret              |
	+----------------------------------+----------------------------------+----------------------------------+
	| 5aedc40cfb3849e59b8302290a329476 | 56cf58837b3d4d248f7dc0e4ae924b76 | cfb8a0a55e5143aaada7d42df0d578ba |
	| feb0ed016a4f4658a795cd168128402e | 247a7f6eca84452ab9c3be0db18ddd7b | 4d761ff6508c417abab5e523d46d60ac |
	+----------------------------------+----------------------------------+----------------------------------+

But which one is my current tenant? Find out the tenant ID from executing `keystone token-get` command. Other ways of doing this include opening a new shell, becoming an admin user there and running a `keystone tenant-list`, or getting the Tenant ID by logging in to Horizon dashboard.

Note the access and secret keys.
In my case, the tenant is `feb0ed016a4f4658a795cd168128402e`, access key is `247a7f6eca84452ab9c3be0db18ddd7b`, and secret key is `4d761ff6508c417abab5e523d46d60ac`.

Let's get started with the `boto` client for consuming AWS APIs. I prefer `ipython` shell, for its interactive features, but normal python shell is just fine too. (Install ipython as `sudo apt-get install ipython`).

Import necessary module

	In [1]: import boto.ec2

Create a `region` object for use in next step.

	In [4]: region = boto.ec2.regioninfo.RegionInfo(name="nova", endpoint='127.0.0.1')
where `nova` is the default availability zone, and endpoint is the IP of the interface on which your DevStack endpoints are created.



* installing and importing boto
* keystone get keys
* commands to connect via boto
* get_all * for listing all resources
* how to create and get instances out of reservations
* 
