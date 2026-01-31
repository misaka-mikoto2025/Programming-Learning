fish_vi_key_bindings

function fish_prompt
	set -l last_status $status
	set -l cyan (set_color cyan)
	set -l pink (set_color magenta)
	set -l blue (set_color blue)
	set -l normal (set_color normal)
	set -l red (set_color red)
	set -l yellow (set_color yellow)
	set -l green (set_color green)

	echo -s $red (prompt_pwd) $normal
	echo -n -s "$cyan> $normal"

	if git rev-parse --git-dir >/dev/null 2>&1
		set -l branch (git branch --show-current 2>/dev/null)
		echo -n -s "$cyan($branch) $normal"
	end

	# 猫娘开场白 （随机）
	set -l greetings "==(^`_`^)=="


	echo -n -s $pink $greetings " "

	# 显示当前目录
	echo -n -s $cyan (prompt_pwd) " "

	# 显示Git状态（如果有）
	if git rev-parse --git-dir >/dev/null 2>&1
		set -l branch (git branch --show-current 2>/dev/null)
		echo -n -s "$cyan($branch) $normal"
	end

	# 错误状态提示
	if test $last_status -ne 0
		# 随机错误提示
		set -l error_msgs
		set -a error_msgs "喵呜～刚才出错了喵"
		set -a error_msgs "命令失败了喵～"
		set -a error_msgs "主人，这个好像不行喵"
		set -a error_msgs "喵？这个命令不对啦"
		set -a error_msgs "出、出错了喵！"
		set -a error_msgs "命令不是这样写的啦喵～"

		set -l error_msg $error_msgs[(random 1 (count $error_msgs))]
		echo -n -s $red $error_msg
		echo ""
		echo -n -s $red ">>" $normal
	else
		# 成功时的随机猫娘提示
		set -l success_msgs "喵～成功了！"
		set -l success_msgs "好厉害喵🐱！"
		set -l success_msgs "主人好棒～"
		set -l success_msgs "完成了～"

	end
	echo -n " "
end
