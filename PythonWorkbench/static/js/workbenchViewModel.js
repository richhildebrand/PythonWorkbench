var workbenchViewModel  = new kendo.data.ObservableObject({
	UnitTests: new Array(),
	userCodeSegment: "",

	reset: function() {
		this.set("userCodeSegment", "");
		var tests = this.get("UnitTests");
		while (tests.length > 0) {
			tests.pop();
		}
	},

	ifThereAreUnitTests: function() {
		return (this.get("UnitTests").length > 0) ? "block" : "none";
	},

	loadExpectedResults: function(tests) {
	var unitTests = this.get("UnitTests"); 
		for (var test in tests) {
			unitTests.push(new UnitTest(test, tests[test]));
		}
	},

	ifAllTestsPass: function() {
		var unitTests = this.get("UnitTests");
		var allPass = true;
		for (var test in unitTests) {
			if (unitTests[test].expectedResult != unitTests[test].actualResult) {
				allPass = false;
			}
		}
		return (allPass) ? "block" : "none";
	},

	getMethodCallTextFromUnitTests: function() {
		var tests = this.get("UnitTests");
		var methodCalls = ""
		if (tests) {
			var testNames = [];
			for (var i=0; i<tests.length; i++) {
				testNames.push(tests[i].name)
			}
			methodCalls = testNames.join("\n");
		}	
		return methodCalls;
	},

	unitTestResult: function(test) {
		var testResult;
		if (test.expectedResult === test.actualResult) {
			testResult = "testPassed"
		}
		else if (test.actualResult !== "") {
			testResult = "testFailed"
		}
		else {
			testResult = "testPending"
		} 
		return testResult;
	},

	loadActualResults: function(tests) {
		var unitTests = this.get("UnitTests");
		for (var test in tests) { 
						var targetTest = _.find(unitTests, function(possibleTest) { 
							return possibleTest.name === test; 
						});
						targetTest.set("actualResult", tests[test]);
		}; 
	},

  	highlightCurrentLine: function(nextLine) {
  		(currentLine.isUserCodeLine) ? pythonCodeEditor.setLineClass(currentLine.line, null, null)
  									 : unitTestEditor.setLineClass(currentLine.line, null, null);
  		
  		nextLine += -1 // setLineClass sets the class on line number + 1
  		if (nextLine >= pythonCodeEditor.lineCount()) {
  			nextLine = nextLine -  pythonCodeEditor.lineCount()
  			if (unitTestEditor.getLineHandle(nextLine)) {
	      		currentLine.line = unitTestEditor.setLineClass(nextLine, null, "currentLine");
	      		currentLine.isUserCodeLine = false;
    		}
  		}
  		else {
  			if (pythonCodeEditor.getLineHandle(nextLine)) {
      			currentLine.line = pythonCodeEditor.setLineClass(nextLine, null, "currentLine");
      			currentLine.isUserCodeLine = true;
    		}
		}			
  	}
});