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

var displayResultData = function(data) {
	lolStringConcats(data.exception, data.localVars,data.stackInfo );
	
	if (data.testResults) {
		workbenchViewModel.loadActualResults(data.testResults);

	}
	workbenchViewModel.highlightCurrentLine(parseInt(data.lineNumber));
};

var lolStringConcats = function(exceptions, localVars, stackInfo) {
	var counter = 0;
	var htmlString = '';

	sortedStackInfo = sortByKey(stackInfo);
	
	if (!exceptions) {
		$('#ResultData').empty();
		for (func in sortedStackInfo){
			backgroundColorClass = (counter % 2 == 0) ?	"oddStackElement" : "evenStackElement";
			counter++;

			var functionName = func.split(') ')[1] + ':';
			var functionVars = sortedStackInfo[func].split(',')
			htmlString =  '<div class="' + backgroundColorClass + '">' 
			htmlString += '<span class="functionName">' + functionName + '</span>'
			
			for (var varAndValue in functionVars) {
				htmlString += '<span class="varAndValue">' + functionVars[varAndValue] + '</span>' 
			}
			htmlString += '</div>'

			$('#ResultData').append(htmlString);
		}
	}
	else {
		htmlString = '<p class="exceptions">' + exceptions + '</p>'
		$('#ResultData').empty();
		$('#ResultData').append(htmlString);
	}
}

function sortByKey(dict) {

    var sorted = [];
    for(var key in dict) {
        sorted[sorted.length] = key;
    }
    sorted.sort();

    var tempDict = {};
    for(var i = 0; i < sorted.length; i++) {
        tempDict[sorted[i]] = dict[sorted[i]];
    }

    return tempDict;
}