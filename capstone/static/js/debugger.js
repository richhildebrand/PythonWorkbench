$('#SimpleDemo').click(function() {
	clearAll();
	var userCodeSegment = 'a = 3\nb = 4\nc = a + b\nd = a + b * c';
	workbenchViewModel.set("userCodeSegment", userCodeSegment);
	loadEditorText();
});

$('#ClearAll').click(function() {
	clearAll();
});

var clearAll = function() {
	$('#ResultData').text("");
	pythonCodeEditor.setValue("");
	unitTestEditor.setValue("");
	workbenchViewModel.reset();
}

var loadEditorText = function() {
	pythonCodeEditor.setValue(workbenchViewModel.userCodeSegment);
	unitTestEditor.setValue(workbenchViewModel.getMethodCallTextFromUnitTests());
};

$('#startDebugging').click(function() {
	var pythonCode = { pythonCode: pythonCodeEditor.getValue, unitTests: unitTestEditor.getValue() };
	$.get('/student/startDebugging', pythonCode, function(data) {
		displayResultData(data)
	});
});

$("#TakeStep").click(function() {
  $.get('/student/takeStep', function(data) {
		displayResultData(data)
	});
});

$('#runAll').click(function() {
	var pythonCode = { pythonCode: pythonCodeEditor.getValue, unitTests: unitTestEditor.getValue() };
	$.get('/student/runAll', pythonCode, function(data) {
		displayResultData(data)
	});
});

var displayResultData = function(data) {
	//var text = 
	lolStringConcats(data.exception, data.localVars,data.stackInfo );
	
	if (data.testResults) {
		workbenchViewModel.loadActualResults(data.testResults);

	}
	workbenchViewModel.highlightCurrentLine(parseInt(data.lineNumber));
};

var lolStringConcats = function(exceptions, localVars, stackInfo) {
	var text = Array();
	var counter = 0;
	var colors = Array('#88E3FC', '#E8E8A5', '#63C1FF');
	var htmlString = '';
	
	if (!exceptions) {
		$('#ResultData').empty();
		for (func in stackInfo){
			text[counter] = func + ': ' + stackInfo[func] + '\n';
			//$('#ResultData').css('background-color', '#0F3');
			htmlString = '<p id="' + counter + '">Function: ' + text[counter] + '</p>'
			//console.log(htmlString);
			counter++;
			//$('#ResultData').empty();
			$('#ResultData').append(htmlString);
		}
	}else{
		htmlString = '<p id="exceptions">' + exceptions + '</p>'
		$('#ResultData').empty();
		$('#ResultData').append(htmlString);
		$('#exceptions').css('background-color', '#F22');
	}
	if(counter) {
		while(counter>=0) {
			$('#'+counter).css('background-color', colors[(counter % 3)]);
			//console.log(colors[counter]);
			//console.log($('#counter').attr());
			counter--;
		}
	}
	//return text;
}