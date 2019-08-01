[![Build Status](https://travis-ci.com/vpetrigo/selenium-langs.svg?branch=master)](https://travis-ci.com/vpetrigo/selenium-langs)

# Chrome language switch with CLI

Demonstration on how to use Chrome `--lang` CLI switch to set up browser language in Selenium tests
without using of the following code:

```python
options = ChromeOptions()
options = options.add_experimental_option("prefs", {"intl.accept_languages": language_to_use})
```