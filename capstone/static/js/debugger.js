$('#SimpleDemo').click(function() {
	var methodBody = 'a = 3\nb = 4\nc = a + b\nd = a + b * c';
	loadAllData(methodBody, "");
});

$('#ClearAll').click(function() {
	loadAllData("", "");
});

var loadAllData = function(methodBody, methodCalls) {
	$('#ResultData').text("");
	$('#PythonCode').text(methodBody);
	$('#MethodCalls').text(methodCalls);
};

$('#startDebugging').click(function() {
	var pythonCode = { pythonCode: $('#PythonCode').val() + '\n' + $('#MethodCalls').val() };
	$.get('/student/startDebugging', pythonCode, function(data) {
		displayResultData(data)
	});
});

$("#TakeStep").click(function() {
  $.get('/student/takeStep', function(data) {
		displayResultData(data)
	});
});

var displayResultData = function(data) {
	$('#ResultData').text(data.exception + data.localVars + data.lineNumber);
};

