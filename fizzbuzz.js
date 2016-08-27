function main(input) {
	var input = input.split("\n");
	var N = parseInt(input[0]), TS = input[1];
	TS = TS.split(" ")
	for (var i = 0; i < N; i++) {
		var T = parseInt(TS[i]);
		for (var j = 1; j <= T; j++) {
			var line = "";
			if(j % 3 == 0 && j % 5 == 0) line = "FizzBuzz";
			else if(j % 3 == 0) line = "Fizz";
			else if(j % 5 == 0) line = "Buzz";
			else
				line = j
			process.stdout.write(line + "\n");
		}
	}
}

process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
	stdin_input += input;
});

process.stdin.on("end", function () {
	main(stdin_input);
});
