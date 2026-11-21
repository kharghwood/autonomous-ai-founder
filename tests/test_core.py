from pathlib import Path
import tempfile
import app.core as core

def test_slugify():
    assert core.slugify('Quick Price Calculator!') == 'quick-price-calculator'

def test_all_five_mvp_templates_pass_basic_checks():
    original = core.PRODUCTS
    with tempfile.TemporaryDirectory() as tmp:
        core.PRODUCTS = Path(tmp)
        try:
            for tool_type in ('calculator', 'estimator', 'checklist', 'text_tool', 'planner'):
                idea = {'name': f'Demo {tool_type}', 'description': 'A small demo', 'problem': 'A simple task', 'tool_type': tool_type}
                product = core.build(idea, [])
                result = core.check_product(product)
                assert result['passed'], result['checks']
                assert (product / 'index.html').exists()
        finally:
            core.PRODUCTS = original