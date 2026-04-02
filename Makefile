init:
	pip install pre-commit
	pre-commit install --hook-type pre-push
	@echo "✅ 环境配置完毕，Git Hook 已自动挂载！"
