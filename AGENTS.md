# AGENTS.md

## Django Portfolio Project

This is a Django-based portfolio website using Bootstrap 5 for responsive design.

### HTML Template Development with Emmet

When generating or editing HTML in Django templates:

- **Use Emmet abbreviations** for rapid HTML generation, especially for Bootstrap components
- **Examples**:
  - `div.container>h1.display-4{Title}+p.lead{Description}` for hero sections
  - `div.row>(div.col-lg-6>p{Content})*2` for grid layouts
  - `btn.btn-primary{Button Text}` for Bootstrap buttons
- **Ensure valid structure**: Avoid nesting block elements (like `<div>`) inside inline elements (like `<h1>`)
- **Django integration**: Emmet works seamlessly in `.html` template files
- **Bootstrap focus**: Leverage Emmet to quickly scaffold Bootstrap 5 components and layouts

### Key Files
- [templates/home.html](templates/home.html) - Main homepage template
- [portfolio_main/views.py](portfolio_main/views.py) - View logic
- [portfolio_main/settings.py](portfolio_main/settings.py) - Django configuration

### Development Workflow
- Use `python manage.py runserver` to start the development server
- Templates are in the `templates/` directory
- Static files (when added) will be in `static/` directory</content>
<parameter name="filePath">d:\portfolio\AGENTS.md