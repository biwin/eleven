# import django
#
# print django.VERSION


from django.template import Template, Context

raw_template = """
<!DOCTYPE html>
<html>
<head lang="en">
	<meta charset="UTF-8">
	<title>Order Notice</title>
</head>
<body>
	<h1>Order Notice</h1>
	<p>Dear {{ person_name }}</p>
	<p>Thanks for placing an order from {{ company }}. Its Shedules to ship on {{ ship_date|date:"F j, Y" }}.</p>
	<p>Here are the items you've ordered:</p>
	<ul>
		{% for item in item_list %}
		<li>{{ item }}</li>
		{% endfor %}
	</ul>
		{% if ordered_warranty %}
			<p>Your warranty information is included in the package</p>
		{% else %}
			<p>You don't have warranty, so just take care of your stuff by your own, dont just bother us if they got failed.</p>

		{% endif %}

	<p>Sincerely <br/> {{ company }}</p>
</body>
</html>"""

t = Template(raw_template)
import datetime


c = Context({
	'person_name': 'John Bounds',
	'Company': 'Google.Inc',
	'ship_date': datetime.date(2014, 9, 2),
	'ordered_warranty': False
})

t.render(c)