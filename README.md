# CivOmega: FDA Search Module

A simple module for [CivOmega][civomega_repo]. See
[the CivOmega repo][civomega_repo].

* **CivOmega Demo**: http://www.civomega.com/
* **CivOmega Repo**: https://github.com/CivOmega/civomega

[civomega_repo]: https://github.com/CivOmega/civomega

---

This module queries the [FDA](https://open.fda.gov)'s
APIs. When using this module (**note: it's installed in CivOmega by default**)
you'll need to have [an API key](https://open.fda.gov/api/reference/#your-api-key).

Once you have the API key, make sure you do this…

```shell
export FDA_API_KEY=$YOUR_KEY_HERE
```

…before running the CivOmega server (`python manage.py runserver`).
