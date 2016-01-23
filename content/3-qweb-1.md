Title: QWEB demystification, Part 1 - t-field and t-esc
Date: 2016-01-16 11:26 
Modified: 2016-01-16 11:26 
Category: Odoo
Tags: QWEB, safe-eval, openerp, odoo, odoo reports
Slug: qweb-1
Authors: Pouya MN
Summary: the differences bitween t-field and t-esc, where and how to use? What about other 't's?

When I stated to make some QWEB reports, I was wondering why there are both `t-field` and `t-esc`? For example both `t-esc="partner_id.name"` and `t-field="partner_id.name"` has the exact same output. 

I made a thorough study and I'll tell you the results, but first... Let me write about QWEB, the great html templating engine. 
There are some templating language, and some of them are XML-based like Genshi, Thymeleaf or Facelets. But QWEB is exactly designed for Odoo, it has access to the database and python side and context. Other templating engines are more general than QWEB and the can normally access to some kind of context passed in a JSON object only. 
The beauty of QWEB is that it is python integrated, there are not just variables but also you can have some python expressions and also it has customizable widgets. I'll write about widgets and using expressions to change the html dynamically.
Appologies me for talking too much, lets get back to the story, `t-esc` or `t-field`. The differences are quite a few, in text fields they are just the same but it is not going on like this with the others. The difference is in the interpreter of them and the widgets.`t-esc` actually calls a `safe-eval` most of other 't's do the same but `t-field` can acept only a field name, or a chain of dot seperated related fields. Also, `t-field` uses form widgets for rendering the selected field while `t-esc` only returns a simple python output (we can change this and prettify the otherwise blunt `t-esc`, I'll talk about it in the following parts). For example if you call t-esc on a related field i.e. `t-esc="someMany2Onefield"` it will print the python `__str__` of the class and a record number, just like what you will have if you in python:
```python 
print self.someMany2Onefield
```
`>>>someMany2Onefield(12,)`
but if you use `t-field` it will display the `display_name` field or the `name_get`. The difference is `t-field` uses form widget of the field as i said before. The same goes with the numerical fields, `t-field` will use the `digits` property of the field for decimal point and it will use thousend separator and other settings from the language settings of Odoo, while `t-esc` simply print the number without formatting (although one can use python's `format` function in `t-esc`).
Other 't' tags also use safe_eval, `t-set` in `t-value` part, `t-if`,  `t-foreach`, `t-att` and `t-attf`, `t-raw` and `t-log`.

#### What can be used in safe_eval
`qweb_context` and of course safe python commands! It raises two questions, what are _safe_ python commands and what is in `qweb_context`?

