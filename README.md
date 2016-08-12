To make changes:
* Download and install the AppEngine SDK: https://cloud.google.com/appengine/downloads
* Test changes locally by:
  * Running ```dev_appserver.py ./``` from the directory of your changes
  * Going to localhost:8080 (or localhost:8080/press-kit, etc)
* To deploy changes
  * Run ```appcfg.py -A pissoffnyc -V v1 update ./``` from the directory of your changes
