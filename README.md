**LAST UPDATED:** June 29, 2025 05:04 AM UTC
# heroku-buildpack-firefox-geckodriver

This buildpack downloads and set's up Mozilla Firefox & Mozilla Geckodriver for your buildpack. You can run Selenium along with your favorite languages, such as Python, Ruby, and Node, to utilize Firefox.

This buildpack ensures it always builds with the latest version of Mozilla Firefox & Geckodriver.

## Installation:

To install and integrate the buildpack with your application running on Heroku's dyno:

```
$ heroku create --buildpack https://github.com/zibdie/heroku-buildpack-firefox-geckodriver

# or if your app is already created:
$ heroku buildpacks:add https://github.com/zibdie/heroku-buildpack-firefox-geckodriver

$ git push heroku master
```

## Configurations:

Update Heroku's environment variables to store the following path strings.

**FIREFOX_BIN**: _/app/vendor/firefox/firefox_

**GECKODRIVER_PATH**: _/app/vendor/geckodriver/geckodriver_

**LD_LIBRARY_PATH**: _/usr/local/lib:/usr/lib:/lib:/app/vendor_

**PATH**: _/usr/local/bin:/usr/bin:/bin:/app/vendor/_

# F.A.Q

## Will this buildpack always be updated? When was the last time this build-pack was built?

This buildpack will **always** have the latest version of Mozilla Firefox & Mozilla Geckodriver. This repository is set to update once a week automatically and will support the latest Heroku slugs and Mozilla Firefox + Geckodriver.

The `/bin/compile` will always have the last time it was checked for a version, on the top of the file.

```
#!/usr/bin/env bash
# bin/compile <build-dir> <cache-dir>
# Last updated: August 02, 2022 01:39 PM UTC
```

## Im having trouble running this buildpack. What should I do?

Do not hesitate to open an issue on this repository.
