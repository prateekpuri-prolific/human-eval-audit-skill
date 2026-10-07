"""Paths and settings for the benchmark harness. Override with environment variables."""
import os
from pathlib import Path
PKG=Path(__file__).resolve().parents[2]
WORK=Path(os.environ.get('BENCH_WORKDIR',PKG/'workdir'))
DATASET=Path(os.environ.get('BENCH_DATASET',PKG/'benchmark/dataset'))
SKILL_V1=PKG/'skill/archive/v1/audit-human-eval-study'
SKILL_V2=PKG/'skill/audit-human-eval-study'
SKILL_V21=PKG/'benchmark/skill-variants/v2.1/audit-human-eval-study'
TASK_TEMPLATE=PKG/'benchmark/harness/task_template'
JUDGE_MODEL=os.environ.get('JUDGE_MODEL','openai/gpt-6-sol')
