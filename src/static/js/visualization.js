
// Set up the canvas
let startTime;
let animationTimeout;
var canvas;
var barWidth;
var barSpacing=10;
let swapPosition=[];
let comparePosition=[];
let extraColors=[];
let extraColors2=[];
let sortedColors=[]
let ANIMATION_SPEED_MS = 1000;





function setup() {
  canvas = createCanvas(850, 500);
  canvas.parent("canvasContent");

  barWidth = 75;

}

// Draw the bars
function draw() {
  background(255,255,255);
  for (var i = 0; i < array.length; i++) {

    if (swapPosition.includes(i)){
      fill(239,92,61)
    }

    else if(comparePosition.includes(i)){
      fill(237,244,100)
    }
	  else if(extraColors.includes(i)){
		fill(98,132,216)
	}
  else if(extraColors2.includes(i)){
		fill(232,229,31)
	}
  else if(sortedColors.includes(i)){
    fill(74,231,84)
  }
    else{
      fill(0);
    }
    stroke(100, 143, 143);
    rect(i * barWidth , 0, barWidth-10, array[i]);
    fill(0);
    stroke(0,0,0);
    textAlign(CENTER);
    text(array[i], i * barWidth + barWidth / 2 -5, array[i] + 15);

    // change the fill color to white
    //text(array[i], i * (barWidth + barSpacing) + barWidth / 2 -5, array[i] * 10 - 5);  // draw the text above the bar
  }
}




// Call the checkTaskStatus function when the page loads
$(document).ready(function() {
  checkTaskStatus("{{ task_id }}");
});



// Define the update function
function mergeSort(animations) {
  document.getElementById("start-button").disabled = true;
  document.getElementById("speedSlider").disabled = true;
	//Working splits
	splits=[];
  // Iterate over the animations
  for (var i = 0; i < animations.length; i++) {
    // Use a closure to preserve the value of i
    (function(i) {
      setTimeout(function() {

		//Split colors
        comparePosition=[];



		//Merge colors
        swapPosition=[]
        var animation = animations[i];

        if(animation[0]==='step' || animation[2]==='step'){
          changeStateBackgroundColor(animation[3])
        }

        if(animation[0]==='test'){
          extraColors2=[animation[1],animation[2]];
        }

		if(animation[0]==='split'){
      extraColors2=[];
			//Working split colors
			extraColors=[];

			//Color split bars
			comparePosition = animation[1];

			//Add split into array in order to use them as working split
			splits.push(animation[1]);
		}

		if(animation[0]==='merge'){

			//Color bars at actual merging split
			extraColors=splits.at(-1)

			var index = animation[1][0];
        	var value = animation[1][1];

			//Swap bars and color
			swapPosition = [index];
			array[index] = value;

			//Delete last split if its same as merge index in order to change splits
			if(index===extraColors.at(-1)){
				splits.pop();
			}


		}

        // Clear colors after animations ends
        if(i+1 === animations.length){
			extraColors=[];
        	comparePosition=[];
        	comparePosition2=[];
			swapPosition=[];
      changeStateBackgroundColor(-1)
        }
      }, ANIMATION_SPEED_MS*i);  // delay by milliseconds for each iteration
    })(i);
  }
}


function bubbleSort(animations) {
    document.getElementById("start-button").disabled = true;
    document.getElementById("speedSlider").disabled = true;

    // Iterate over the animations
    for (var i = 0; i < animations.length; i++) {
      // Use a closure to preserve the value of i
      (function(i) {

        animationTimeout = setTimeout(function() {
          comparePosition=[];
          swapPosition=[]
          var animation = animations[i];


          //highligh bars that are being compared

          if(animation[0]==='sorted'){
            sortedColors = animation[1];
        }
          if(animation[0]==='step' || animation[3]==='step'){
            changeStateBackgroundColor(animation[4])
          }

          if(animation[0]==='compare'){
            comparePosition=[animation[1],animation[2]];
          }

          if(animation[0]==='swap'){
            var temp = array[animation[1]];
            array[animation[1]] = array[animation[2]];  //animation[2] is second index, and animation[1] is first index
            array[animation[2]] = temp;
            swapPosition = [animation[1],animation[2]];
          }

          if(i+1 === animations.length){

            comparePosition=[]
            sortedColors=[]
            changeStateBackgroundColor(-1)
          }

        }, ANIMATION_SPEED_MS*i);  // delay by 250 milliseconds for each iteration
      })(i);
    }
  }


function selectionSort(animations){
  document.getElementById("start-button").disabled = true;
  document.getElementById("speedSlider").disabled = true;
  // Iterate over the animations
  for (var i = 0; i < animations.length; i++) {
    // Use a closure to preserve the value of i
    (function(i) {
      setTimeout(function() {
        var animation = animations[i];
        var firstIndex = animation[1];
        var secondIndex = animation[2];

        comparePosition=[];
        swapPosition=[]

        if(animation[0]==='sorted'){
          sortedColors = animation[1];
      }

          if(animation[0]==='step' || animation[3]==='step'){
            changeStateBackgroundColor(animation[4])
          }

		if(animation[0]==='compare'){
			comparePosition = [firstIndex];
      extraColors=[secondIndex]
		}

		if(animation[0]==='swap'){
      extraColors=[];
      comparePosition=[];
            swapPosition=[firstIndex];
            [array[secondIndex],array[firstIndex]] = [array[firstIndex],array[secondIndex]];
            swapPosition=[firstIndex];

		}

        // Clear colors after animations ends
        if(i+1 === animations.length){
			extraColors=[];
      sortedColors=[];
        	comparePosition=[];
			swapPosition=[];
      changeStateBackgroundColor(-1)
        }
      }, ANIMATION_SPEED_MS*i);  // delay by milliseconds for each iteration
    })(i);
  }
}


function radixSort(animations){
  // Iterate over the animations
  for (var i = 0; i < animations.length; i++) {
    // Use a closure to preserve the value of i
    (function(i) {
      setTimeout(function() {
        var animation = animations[i];
        var firstIndex = animation[1];
        var valueToSwap = animation[2];

        comparePosition=[];
        swapPosition=[];


		if(animation[0]==='compare'){
			comparePosition = [firstIndex];

		}

		if(animation[0]==='swap'){
      oldIndex = animation[3];
      swapPosition = [firstIndex];
      array[firstIndex] = valueToSwap;


		}

        // Clear colors after animations ends
        if(i+1 === animations.length){
			extraColors=[];
        	comparePosition=[];
			swapPosition=[];
        }
      }, ANIMATION_SPEED_MS*i);  // delay by milliseconds for each iteration
    })(i);
  }
}

function quickSort(animations){
  // Iterate over the animations
  for (var i = 0; i < animations.length; i++) {
    // Use a closure to preserve the value of i
    (function(i) {
      setTimeout(function() {
        var animation = animations[i];
        var firstIndex = animation[1];
        var secondIndex = animation[2];

        comparePosition=[];
        swapPosition=[];

    if(animation[0]==='pivot'){
          extraColors = [firstIndex];

    }

		if(animation[0]==='compare'){
			comparePosition = [firstIndex,secondIndex];

		}

		if(animation[0]==='swap'){
      swapPosition = [firstIndex,secondIndex];
      [array[firstIndex],array[secondIndex]] = [array[secondIndex],array[firstIndex]];


		}

        // Clear colors after animations ends
        if(i+1 === animations.length){
			    extraColors=[];
        	comparePosition=[];
			    swapPosition=[];
        }
      }, ANIMATION_SPEED_MS*i);  // delay by milliseconds for each iteration
    })(i);
  }
}

function insertionSort(animations){
  document.getElementById("start-button").disabled = true;
  document.getElementById("speedSlider").disabled = true;
  // Iterate over the animations
  for (var i = 0; i < animations.length; i++) {
    // Use a closure to preserve the value of i
    (function(i) {
      setTimeout(function() {
        var animation = animations[i];

        comparePosition=[];
        swapPosition=[]

    if(animation[0]==='step' || animation[2]==='step' || animation[3]==='step'){
          changeStateBackgroundColor(animation[4])
      }

    if(animation[0]==='sorted'){
          sortedColors = animation[1];
      }

    if(animation[0]==='key'){
            extraColors = [animation[1]];
          }

		if(animation[0]==='compare'){
			comparePosition = [animation[1]];
		}

		if(animation[0]==='swap'){

      [array[animation[2]],array[animation[1]]] = [array[animation[1]],array[animation[2]]];
      extraColors = [animation[2]];
      swapPosition=[animation[1],animation[2]];

		}

        // Clear colors after animations ends
        if(i+1 === animations.length){
			extraColors=[];
        	comparePosition=[];
			swapPosition=[];
			sortedColors=[];
      changeStateBackgroundColor(-1)
        }
      }, ANIMATION_SPEED_MS*i);  // delay by milliseconds for each iteration
    })(i);
  }
}
