# Resource Counter

**its powerful tool to Calculating the raw materials for something you want to build**.

- you can use it for any item or recipe you need.
- This program can store the recipes you give it and use them to expand the ingredients.

<hr>

<h3>Adding recipe</h3>

```bash
python __main__.py -r "4*torch:1*coal, 1*stick"
```

<hr>

<h3>Calculating raw materials</h3>

- We need 64 of torch How many resources does it require?
    - ```bash
        python __main__.py -e torch -c 800
      ```
- or this for minecraft stack size
    - ```bash
        python __main__.py -e torch -c 800 -mc
      ```
