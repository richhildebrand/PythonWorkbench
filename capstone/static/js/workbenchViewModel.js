var workbenchViewModel  = new kendo.data.ObservableObject({
	Exercise: new Exercise(),
	UnitTests: new Array(),

	reset: function() {
		var tests = this.get("UnitTests");
		while (tests.length > 0) {
			tests.pop();
		}
	},

	loadNewExercise: function(wordProblem, methodBody, methodCallText) {
		exercise = this.get("Exercise");
		exercise.set("wordProblem", wordProblem);
		exercise.set("methodBody", methodBody);
		exercise.set("methodCallText", methodCallText);
	},

	loadExpectedResults: function(tests) {
	this.reset()
	unitTests = this.get("UnitTests"); 
		for (var test in tests) {
			unitTests.push(new UnitTest(test, tests[test]));
		}
	},

	loadActualResults: function(tests) {
		unitTests = this.get("UnitTests");
		for (test in tests) { 
						var targetTest = _.find(unitTests, function(possibleTest) { 
							return possibleTest.name === test; 
						});
						targetTest.set("actualResult", tests[test]);
		}; 
	},

	highlightCurrentLine: function(lineToHighlight) {
		// the class is sent on given line number + 1
		lineToHighlight = parseInt(lineToHighlight)-1;
		$('.currentLine').removeClass('currentLine');
		pythonCodeEditor.setLineClass(lineToHighlight, undefined, 'currentLine');
	}
});