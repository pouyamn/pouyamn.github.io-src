Title: Would you like 'like' and 'ilike' in your _domain_ and _attr_?
Date: 2016-01-23 21:26 
Modified: 2016-01-23 21:26 
Category: views
Tags: views,odoo,JS,hackish
Slug: view_domain_add_like
Authors: Pouya MN
Summary: how to add 'like' and 'ilike' operators to domains in odoo


The point is domain calculations (attrs is also using domain) are done in JS not the database, so you can not use SQL commands such as 'ilike'.

But there is a way to add this function to Odoo rather easily with some coding. Edit `view_form.js` ( in openerp/addons/web/static/src/js), find this line:
```js
            case 'not in':
                if (!_.isArray(val)) val = [val];
                stack.push(!_(val).contains(field_value));
                break;
```
and add these lines after it:

```js
            case 'like':
                stack.push(field_value.indexOf(val)>=0);
                break;
            case 'not like':
                stack.push(field_value.indexOf(val)<0);
                break;
            case 'ilike':
                stack.push(field_value.toUpperCase().indexOf(val.toUpperCase())>=0);
                break;
            case 'ilike':
                stack.push(field_value.toUpperCase().indexOf(val.toUpperCase())<0);
                break; 
```
and save it, TADA you can use it now. 
warning: if you use it with a field which is not string, it will cause an error


