from app.core import slugify, check_product
from pathlib import Path
import tempfile
def test_slugify():
    assert slugify("Quick Price Calculator!")=="quick-price-calculator"
def test_product_check():
    with tempfile.TemporaryDirectory() as d:
        p=Path(d); (p/"index.html").write_text('<!doctype html><html><head><meta name="viewport"></head></html>')
        assert check_product(p)["passed"]
