---
layout: default
lang: en
title: Blog
permalink: /blog/
---

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <small>{{ post.date }}</small>
    </li>
  {% endfor %}
</ul>
