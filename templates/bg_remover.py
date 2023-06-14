{% extends "base.html" %}
{%load static%}
{% block title%}
<title>portfolio</title>
{% endblock %}

{% block nav%}
<nav class="md:flex m-8 bg-grey  sticky top-0 -mb-12"> 
		<div class="md:flex-auto w-32">
			<a href="/"><img src="{% static 'images/logo.png'%}" alt="logo" class="h-20"></a>
		</div>
</nav>
{%endblock%}
{% block content%}

<div class="flex justify-between ">
    <div class="">
        <div class="text-2xl pt-20 text-yellow-400 break-after-column">
            <p>Hello _ _ _,</p>
        </div>
        <br>
        <div class="text-7xl ">
            <p><b>I`m PMK</b></p>
        </div>
        <div class="flex ml-52 mt-5">
            <button class="bg-blue-500 p-2 rounded-lg text-white mr-2">Download CV</button>
            <button class="bg-blue-500 p-2 rounded-lg text-white">Contact me</button>
        </div>
    </div>
    <div class="w-2/4">
   <div class="flex text-center">
        <button class="bg-blue-500 px-4 py-2 text-white rounded-lg inline-block mx-auto">About me</button>
        <button class="bg-blue-500 px-4 py-2 text-white rounded-lg inline-block mx-auto">Projects</button>
        <button class="bg-blue-500 px-4 py-2 text-white rounded-lg inline-block mx-auto">Contact</button>
    </div>

    </div>
</div>
</div> 


{% endblock %}

{%block footer%}

{%endblock%}
