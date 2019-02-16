Package Managers and Virtual Environments
posted on 2016.02.04

Python, Ruby, Node.js, and Go use package management to make library and application dependencies available to their runtime environment. If you need to use a certain library or utility in your software project, then you use a package manager–such as pip1 or gem2–to install that dependency. The software you are writing will typically have several or many such dependencies. And it is likely that each dependency will be constrained to a particular version, or perhaps a minimum version or a version range.

The problem: conflicting versions
If you have installed other software written using Python, Ruby, Node.js, or Go then you may already have different and conflicting versions of dependent packages installed. There will be breakage as dependencies among different versions of packages and different versions of runtimes collide.

You might be developing multiple software projects that have, between them, conflicting package and dependency requirements. Or you may just be maintaining different versions of the same software project, with conflicting dependencies or conflicting dependency versions between different versions of your software project.

How can you manage the need for multiple sets of dependencies and language versions to be installed on the same system?

The solution: virtual environments
The solution is to use virtual environments. A virtual environment is a way of isolating a particular version of a language runtime along with the packages that need to be installed for that language version and the given purpose. Virtual environments set the language runtime to a particular version, set the package installation locations to a private location, isolate package management from the global package management space, and set the build and runtime search paths to the private locations of the virtual environment.

Each application and each software project can have its own virtual environment. If more than one language ecosystem is in use, then there can be concurrent virtual environments—one for each language ecosystem.

Python virtual environments
Python has the most mature implementation of virtual environments. As of Python 3.3, it is the only one of the four languages considered here that has build virtual environment support directly into its standard library. The rock solid and straightforward virtualenv virtual environment manager is available for both the Python 2 and Python 3 ecosystems.

Ruby virtual environments
Ruby has a mature virtual environment solution using rbenv and Bundler. rbenv is a safer, less intrusive, and more flexible tool than the older (though still in use) rvm. I recommend using rbenv and Bundler over rvm if you can, and I recommend converting any existing use of rvm to rbenv.

Node.js virtual environments
It’s still early days (circa late 2015, early 2016) for Node.js virtual environment management tools. The problem is that a reasonable tool exists for some Unix systems, [nvm][nvm, but cannot be used on Windows systems and has issues with some particular Unix systems and shells. Alternative virtual environment management tools exist for Windows, but seem to me to be awkward to install and use.

Worse, the official Node.js installers for OS X and Windows seem to assume that one should only have a single version of Node.js on a system and it ought to be the latest one available. That policy is in direct conflict with the reasons for using virtual environments.

So I just build (from source) the particular version Node.js that I need, and I copy the resulting install directory into the project. Then I create an activation script that sets appropriate environment variables and search paths to point to that project-local copy of Node.js. A simple solution with no 3rd-party virtual environment manager required. Nice.

Go virtual environments
Go does not have a virtual environment solution that I’m aware of. There is no help from the language itself. I have not worked with Go sufficiently to present here a bullet proof virtual environment solution. But I believe that the same kind of approach I use for Node.js will be necessary with Go.

Activating and deactivating virtual environments
Activating a virtual environment is the process of changing the current execution environment so that all references to the language runtime and tools, and all references to the package installation location, will resolve to the locations local to the virtual environment directories and files within the project directory tree.

Deactivating a virtual environment is the process of restoring the original, non-virtual, execution environment so that all language and package references resolve to the original system locations (if any).

Automating activation and deactivation
To automate the activation and deactivation of the virtual environment, I create a script to “activate” those three environments, and have it generate another script that “deactivates” those environments (and deletes itself).

I usually want such scripts to change the command line prompt to indicate that a virtual environment is active. It’s a great reminder that it may need to be deactivated before you switch to some other project.

Example use case
Imagine that on my system I have Python 2.7 installed and Ruby 2.0.0. I don’t have Node.js installed.

Now I want to create a blog project using a static site generator. The static site generator is written in Python 3.5 and uses Sass which is written in Ruby and needs Ruby 2.2.3. I have a number of additional things I want to automate to manage the static site generation and I want to use Gulp to do that; Gulp requires Node.js.

When I create a new software project on my development system, I will setup scripts that establish the virtual environments needed for that project, that activate that environment, and that deactivate the environment. Going further, within the scripts I use to automate build and test actions, I add checks to make certain that the necessary environment is active and that the required dependencies are installed.

To ensure the correct language versions and package dependencies, I would create a directory for the blog project. Within that directory, I would:

use Python’s virtualenv utility to create a Python 3.5 virtual environment
use the rbenv utility to create a Ruby 2.2.3 virtual environment
download and build Node.js v0.12.7 and copy the installation files to a subdirectory of the project
Then I’d activate the three virtual environments and install all the necessary packages and applications.

Automating upgrades
For long running projects you may want to keep current with the latest upgrades and patches to dependencies. Given that such a task is both tedious to perform manually (especially if there are many packages), and may need to be done multiple times over the lifetime of the project, it makes sense to automate this as well.

Using a script to perform dependency upgrades is a great way to ensure you haven’t missed anything. It also allows you to automate backup of the current virtual environments so that you can roll back if an upgrade breaks your project. Someday you will be glad you built that into your automation.

More
There is certainly more to say on this topic. In subsequent posts, I hope to explore the specifics of virtual environment setup, activation, deactivation, and package updates for each of: Python, Ruby, Node.js, and Go.

Update 2016-04-07: See these additional posts on this topic …

See also:

Using Virtual Environments - Python I
Using Virtual Environments - Python II
Using Virtual Environments - Ruby I
Using Virtual Environments - Ruby II
The Python ecosystem’s package manager. ?

The Ruby ecosystem’s package manager. ?