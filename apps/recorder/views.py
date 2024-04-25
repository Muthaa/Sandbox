import os
from flask import Blueprint, render_template
from apps.recorder import blueprint
from jinja2 import TemplateNotFound


@blueprint.route('/record')
def index():
	return "Recording...."