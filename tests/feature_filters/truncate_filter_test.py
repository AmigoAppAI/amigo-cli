import pytest

from amigo.code_feature import CodeFeature
from amigo.feature_filters.truncate_filter import TruncateFilter


@pytest.mark.asyncio
async def test_truncate_feature_selector(temp_testbed, mock_call_llm_api):
    all_features = [
        CodeFeature(
            temp_testbed / "multifile_calculator" / "calculator.py"
        ),  # 188 tokens
        CodeFeature(
            temp_testbed / "multifile_calculator" / "operations.py"
        ),  # 87 tokens
    ]

    feature_filter = TruncateFilter(100)
    selected = await feature_filter.filter(all_features)
    assert len(selected) == 1
    assert selected[0].path.name == "operations.py"

    feature_filter = TruncateFilter(200)
    selected = await feature_filter.filter(all_features)
    assert len(selected) == 1
    assert selected[0].path.name == "calculator.py"
