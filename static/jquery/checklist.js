
var currId = 0;
stepType; //Taken from createList.html, contains all step types



function addCreateStep(idNum){
	
	var stepNum = document.createElement("label");
	stepNum.innerHTML = idNum+1;
	var stepNumDiv = document.createElement("div");
	stepNumDiv.className = "col-sm-1";
	stepNumDiv.appendChild(stepNum);
	
	var stepName = document.createElement("input");
	stepName.name = "name";
	stepName.className = "form-control";
	stepName.placeholder = "name of step";
	stepName.id = "newStepId"+idNum;
	var stepNameDiv = document.createElement("div");
	stepNameDiv.className = "col-sm-4";
	stepNameDiv.appendChild(stepName);
	
	var selectType = document.createElement("select");
	selectType.className = "form-control";
	for (var i=0;i<stepType.length;i++)
	{ 
		var option = document.createElement("option");
		option.text = stepType[i];
		selectType.appendChild(option);
	}
	var selectTypeDiv = document.createElement("div");
	selectTypeDiv.className = "col-sm-2";
	selectTypeDiv.appendChild(selectType);
	
	var description = document.createElement("input");
	description.placeholder = "description";
	description.className = "form-control";
	var descriptionDiv = document.createElement("div");
	descriptionDiv.className = "col-sm-5";
	descriptionDiv.appendChild(description);
	
	var divRow = document.createElement("div");
	divRow.className = "row form-group";
	divRow.id = "groupStepId"+idNum;
	divRow.appendChild(stepNumDiv);
	divRow.appendChild(stepNameDiv);
	divRow.appendChild(selectTypeDiv);
	divRow.appendChild(descriptionDiv);
	
	
	var createStepsDiv = document.getElementById("create-steps");
	createStepsDiv.appendChild(divRow);
};

function deleteStep(){
	var createSteps = document.getElementById("create-steps");
	createSteps.removeChild(document.getElementById("groupStepId"+currId));
}





addCreateStep(currId);

$("#removeStep").click(function() {
	deleteStep();
	currId --;
});

$("#addStep").click(function() {
	currId ++;						 
	addCreateStep(currId);
	
	
});


