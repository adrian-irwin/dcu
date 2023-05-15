
AB.maxSteps = 1000000;
AB.drawRunControls = false;
ABWorld.drawCameraControls = false;

// set constants
const skycolour = "lightblue";
const boxcolor = "#bbbbbb";
const movespeed = 1;
const delayTime = 750;
const OBJPATH = "/uploads/skellyc4/";	// path of OBJ and MTL
const OBJNAME = "catMod.obj";
const MTLNAME = "catMod-3.mtl";
const SCALE_HERO 		= 0.1;

// set global variables
let moveForward = false;
let moveBackward = false;
let moveLeft = false;
let moveRight = false;
let redOn = false;
let hostStarted = false;
let actualChange = false;
let overallTime = 0;
let consecutiveSameLightChanges = 0;
let host;
let lightTime;
let startTime = performance.now();
let player;

// create both the red and green light audios and set their volume, to be played when the lights change
const greenLightChangeSound = new Audio("/uploads/adrian28/green-light-sound.wav");
greenLightChangeSound.volume = 0.35;
greenLightChangeSound.loop = false;

const redLightChangeSound = new Audio("/uploads/adrian28/red-light-sound.mp3");
redLightChangeSound.volume = 0.15;
redLightChangeSound.loop = false;

//loading in grass textures
const textureLoader = new THREE.TextureLoader();
//load base colour map
const grassBaseColour = textureLoader.load("/uploads/skellyc4/Stylized_Grass_002_basecolor.jpg");
grassBaseColour.wrapS = THREE.RepeatWrapping;
grassBaseColour.wrapT = THREE.RepeatWrapping;
grassBaseColour.repeat.set( 8, 16 );
//load ambient occlusion map
const grassAmbientOcclusionMap = textureLoader.load("/uploads/skellyc4/Stylized_Grass_002_ambientOcclusion.jpg");
grassAmbientOcclusionMap.wrapS = THREE.RepeatWrapping;
grassAmbientOcclusionMap.wrapT = THREE.RepeatWrapping;
grassAmbientOcclusionMap.repeat.set( 8, 16 );
//load displacement map
const grassHeightMap = textureLoader.load("/uploads/skellyc4/Stylized_Grass_002_height.png");
grassHeightMap.wrapS = THREE.RepeatWrapping;
grassHeightMap.wrapT = THREE.RepeatWrapping;
grassHeightMap.repeat.set( 8, 16 );
//load normal map
const grassNormalMap = textureLoader.load("/uploads/skellyc4/Stylized_Grass_002_normal.jpg");
grassNormalMap.wrapS = THREE.RepeatWrapping;
grassNormalMap.wrapT = THREE.RepeatWrapping;
grassNormalMap.repeat.set( 8, 16 );
//load roughness map
const grassRoughnessMap = textureLoader.load("/uploads/skellyc4/Stylized_Grass_002_roughness.jpg");
grassRoughnessMap.wrapS = THREE.RepeatWrapping;
grassRoughnessMap.wrapT = THREE.RepeatWrapping;
grassRoughnessMap.repeat.set( 8, 16 );

//create light source (for textures)
const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.x += 20;
directionalLight.position.y += 20;
directionalLight.position.z += 20;

// create the floor
const floorGeometry = new THREE.PlaneGeometry(100, 200, 1024, 2048);
floorGeometry.rotateX(- Math.PI / 2);
floorGeometry.attributes.uv2 = floorGeometry.attributes.uv;

// create the floor's material
const floorMaterial = new THREE.MeshStandardMaterial({
    map: grassBaseColour,
    normalMap: grassNormalMap,
    displacementMap: grassHeightMap,
    displacementScale: 0.4,
    roughnessMap: grassRoughnessMap,
    roughness: 0.5,
    aoMap: grassAmbientOcclusionMap
});

// create the floor
const floor = new THREE.Mesh(floorGeometry, floorMaterial);
floor.position.set(0, -20, -99);

// create the red light and make it invisible
const redLightGeometry = new THREE.BoxGeometry(20, 20, 5);
const lightMaterial = new THREE.MeshBasicMaterial({ color: "red" });
const redLight = new THREE.Mesh(redLightGeometry, lightMaterial);
redLight.position.set(0, -10, -196);
redLight.visible = false;

// create the green light
const greenLightGeometry = new THREE.BoxGeometry(20, 20, 5);
const greenLightMaterial = new THREE.MeshBasicMaterial({ color: "green" });
const greenLight = new THREE.Mesh(greenLightGeometry, greenLightMaterial);
greenLight.position.set(0, -10, -196);

// create the finish line
const finishLineGeometry = new THREE.BoxGeometry(100, 0.8, 1);
const finishLineMaterial = new THREE.MeshBasicMaterial({ color: "blue" });
const finishLine = new THREE.Mesh(finishLineGeometry, finishLineMaterial);
finishLine.position.set(0, -19.7, -175);

let m = new THREE.MTLLoader();
m.setResourcePath ( OBJPATH );
m.setPath         ( OBJPATH );

// create the player model as a cat then initialise the rest of the scene once we have the cat loaded in
function loadPlayer() {
    m.load ( MTLNAME, function ( materials ) {
    	materials.preload();
    	let o = new THREE.OBJLoader();
    	o.setMaterials ( materials );
    	o.setPath ( OBJPATH );

    	o.load ( OBJNAME, function ( object )
    	{
    		theCat = object;
    		theCat.bumpScale = 0.015;
    		if ( theCat ) {player = theCat; initScene()}
    		else (console.log("No cat :("));
    	});
    });
}

// initialise the full scene once the cat is loaded in
function initScene() {
    // initialise a 3d world
    ABWorld.init3d(150, 1500000, skycolour);

    // add the floor, red light, green light, finish line, player and a light source to the world
    ABWorld.scene.add(floor);
    ABWorld.scene.add(redLight);
    ABWorld.scene.add(greenLight);
    ABWorld.scene.add(finishLine);
	player.position.x = 0;
    player.position.y = -18;
	player.position.z = 0;
	player.rotation.y += 3.14159;
	player.rotation.x += 1.5708;
	player.scale.multiplyScalar ( SCALE_HERO );
    ABWorld.scene.add(player);
    ABWorld.scene.add(directionalLight);

    // set the camera position behind the player for use in MoveWith mode
    ABWorld.lookat.copy(player.position);
    ABWorld.follow = new THREE.Vector3(player.position.x, player.position.y + 6, player.position.z + 10);

    // add event listeners for key presses and releases
    document.addEventListener("keydown", onKeyDown, false);
    document.addEventListener("keyup", onKeyUp, false);

    // set the default camera mode to MoveWith so we follow the player
    ABWorld.cameraMove();

    // remove the loading screen once everything has been added to the scene
    AB.removeLoading();
}

// handle key presses
function onKeyDown(event) {
    switch (event.code) {
        case "KeyW":
            moveForward = true;
            break;

        case "KeyA":
            moveLeft = true;
            break;

        case "KeyS":
            moveBackward = true;
            break;

        case "KeyD":
            moveRight = true;
            break;
    }
}

// handle key releases
function onKeyUp(event) {
    switch (event.code) {
        case "KeyW":
            moveForward = false;
            break;

        case "KeyA":
            moveLeft = false;
            break;

        case "KeyS":
            moveBackward = false;
            break;

        case "KeyD":
            moveRight = false;
            break;
    }
}

// handle player movement
function movementHandler() {
    if ((moveForward || moveBackward || moveLeft || moveRight) && redOn) { // if the player is moving and the red light is on, reset the player's position
        player.position.set(0, -18, -2);
        ABWorld.follow.set(player.position.x, player.position.y + 6, player.position.z + 10);
    }
    else { // otherwise, move the player in the direction they are pressing and update the camera's position
        if (moveForward === true) {
            ABWorld.follow.z -= movespeed;
            player.position.z -= movespeed;
        }
        if (moveBackward === true && player.position.z + movespeed < 0) {
            ABWorld.follow.z += movespeed;
            player.position.z += movespeed;
        }
        if (moveLeft === true && player.position.x - movespeed >= -49) {
            ABWorld.follow.x -= movespeed;
            player.position.x -= movespeed;
        }
        if (moveRight === true && player.position.x + movespeed <= 49) {
            ABWorld.follow.x += movespeed;
            player.position.x += movespeed;
        }
    }
}

// change the light visibility so that the red light is visible and the green light is invisible
function changeToRed() {
    redLight.visible = true; // make the red light visible
    greenLight.visible = false; // make the green light invisible
}

// change the light visibility so that the green light is visible and the red light is invisible
function changeToGreen() {
    redLight.visible = false; // make the red light invisible
    greenLight.visible = true; // make the green light visible
}

// handle the red light
function redLightFunction() {
    AB.socketOut({ "name": "lightChange", "data": { "redOn": true, "actualChange": actualChange } });
    redLightChangeSound.play();
    setTimeout(function() { changeToRed(); redOn = true; }, delayTime);
}

// handle the green light
function greenLightFunction() {
    AB.socketOut({ "name": "lightChange", "data": { "redOn": false, "actualChange": actualChange } });
    greenLightChangeSound.play();
    setTimeout(function() { changeToGreen(); redOn = false; }, delayTime);
}

// handle the light changes
function changeLight() {
    let currentTime = performance.now();
    let occuranceDelta = (currentTime - lightTime) / 1000; // get the time since the last light change

    // if the random boolean is true and the time since the last light change is greater than 3 seconds, change the light
    if (AB.randomBoolean() && occuranceDelta >= 3) {
        let newColour = AB.randomPick("red", "green"); // randomly pick a colour to change the light to

        // based on the randomly chosen colour change the light to that colour either if it is not already that colour or if it has been that colour more than 3 times in a row
        if (newColour === "red") {
            if (redLight.visible === false) {
                consecutiveSameLightChanges = 0;
                actualChange = true;
                redLightFunction();
            }
            else { // if the red light is already visible
                consecutiveSameLightChanges++;
                actualChange = false;
                if (consecutiveSameLightChanges >= 3) {
                    consecutiveSameLightChanges = 0;
                    actualChange = true;
                    greenLightFunction();
                }
            }
        }
        else if (newColour === "green") {
            if (greenLight.visible === false) {
                consecutiveSameLightChanges = 0;
                actualChange = true;
                greenLightFunction();
            }
            else {
                consecutiveSameLightChanges++;
                actualChange = false;
                if (consecutiveSameLightChanges >= 3) {
                    consecutiveSameLightChanges = 0;
                    actualChange = true;
                    redLightFunction();
                }
            }
        }
        lightTime = currentTime; // update the time of the last light change
    }
}

// check if the player has reached the finish line
function checkLocation() {
    if (player.position.z <= -175) {
        AB.msg("<br><font color=red><B>Congratulations! You Win!</B></font>", 2);
        AB.abortRun = true;
        const runTime = Math.floor((performance.now() - startTime) / 1000);
        AB.newSplash();
        AB.splashHtml(
            "<h1>You Won</h1>" +
            `<p>It took you ${runTime} seconds to cross the finish line.</p>` +
            "<p>If you want to play again, click the button below.</p>" +
            "<button onclick='document.location.reload();' class='ab-largenormbutton'>Play Again</button>"
        );
        AB.socketOut({ "name": "finishLineCrossed", "data": { "runTime" : runTime } });
    }
}

AB.socketStart(); // start the socket connection

// everytime a new player joins the game, ensure that the new player is able to click the start game button
AB.socketUserlist = function (array) {
    switch (array.length) {
        case 1:
            host = AB.socket.id;
            AB.msg("<p>You are the Host\n</p>", 1);

            if ($("#splashScreenStartMessage p:contains(You are the host)") !== 1) {
                $("#splashScreenStartMessage").append("<p>You are the host, you must start the game so that others can play too.</p>");
            }

            break;
        default:
            // the host will send a socket message to the new player to tell them if the game has started or not
            if (host !== undefined) {
                AB.socketOut({ "name": "updateHostStarted", "data": { "hostStarted": hostStarted } });
            }
            else {
                if ($("#splashScreenStartMessage p:contains(You must wait until the host)") !== 1) {
                    $("#splashScreenStartMessage").append("<p>You must wait until the host starts the game.</p>");
                }
            }
            $("#splashbutton").html("Click here to start the game");
            $("#splashbutton").prop("disabled", false);

            break;
    }
    // update the number of players message in game
    AB.msg(`<p>Current number of players = ${array.length}\n</p>`, 5);
};

AB.socketIn = function (data) {
    if (data.name === "finishLineCrossed") {
        AB.newSplash();
        AB.splashHtml(
            "<h1>You Lose</h1>" +
            "<p>The player who won the game crossed the finish line in " + data.data.runTime + " seconds.</p>" +
            "<p>If you want to play again, click the button below.</p>" +
            "<button onclick='document.location.reload();' class='ab-largenormbutton'>Play Again</button>"
        );
    }
    if (data.name === "lightChange") {
        if (data.data.redOn) {
            if (data.data.actualChange) {
                redLightChangeSound.play();
            }
            setTimeout(function() { changeToRed(); redOn = true; }, delayTime);
        }
        else {
            if (data.data.actualChange) {
                greenLightChangeSound.play();
            }
            setTimeout(function() { changeToGreen(); redOn = false; }, delayTime);
        }
    }
    if (data.name === "hostPressedStart") {
        hostStarted = true;
        $("#splashbutton").html("Click here to start the game");
    }
    if (data.name === "updateHostStarted") {
        hostStarted = data.data.hostStarted;
        $("#splashbutton").html("Click here to start the game");
    }
    if (data.name === "timer") {
        AB.msg(`<p>Time: ${data.data.time}\n</p>`, 4);
        overallTime = data.data.time;
    }
};

// message to show the user when they join the game
const splashScreenMessage = (
    '<div id="splashScreenStartMessage" style="text-align:center; font-family:Arial, Helvetica, sans-serif;">' +
    '<p>The objective of the game is to get to the <font color=blue><B>blue</B></font> finish line at the other end of the playing area.</p>' +
    '<p style="color: red">When the light is <B>red</B>, you must stop, if you move while the light is red, <B>you will be sent back to the start.</B></p>' +
    '<p style="color: green">When the light is <B>green</B>, you are able to freely move around.</p>' +
    '<p>A <B>sound</B> will play just before the light changes colour.</p>' +
    '<p style="color: blue">Use <B>W</B>, <B>A</B>, <B>S</B>, or <B>D</B> to move around.</p>' +
    '</div>'
);
AB.newSplash(splashScreenMessage); // display the start game message

$("#splashbutton").html("Click here to start the game"); // change the text on the start game button
// when the start game button is clicked, start the game based on if the host has already started the game or not
AB.splashClick(function () {
    if (host !== undefined) { // if the player is the host, start the game
        if (AB.socket && AB.socket.connected) {
            lightTime = performance.now();
            AB.runReady = true;
            AB.removeSplash();
            hostStarted = true;
            AB.socketOut({ "name": "hostPressedStart"});
        }
    }
    else if (host === undefined && hostStarted){ // if the player is not the host and the game has started, start the game
        if (AB.socket && AB.socket.connected) {
            lightTime = performance.now();
            AB.runReady = true;
            AB.removeSplash();
        }
    }
    else { // if the player is not the host and the game has not started, change the button text to tell the player to wait for the host to start the game
        $("#splashbutton").html("Host has not started the game yet");
    }
});

// on initialisation of the world this function is ran
AB.world.newRun = function () {
    // while everything is being added to the scene add a loading screen
    AB.loadingScreen();
    // set the runReady variable to false so that the game does not start until the host has started the game
    AB.runReady = false;

    loadPlayer();
};


// on each step of the world this function is ran
AB.world.nextStep = function () {
    movementHandler();

    // set the camera to look at the player
    ABWorld.lookat.x = player.position.x;
    ABWorld.lookat.y = player.position.y;
    ABWorld.lookat.z = player.position.z;

    checkLocation();

    if (AB.socket.id === host) { // only the host will run this code
        // to make sure that every player sees the same light colour, only the host will change the light colour and will send the new colour to the other players
        changeLight();
        overallTime = Math.floor((performance.now() - startTime) / 1000);
        AB.msg(`<p>Time: ${overallTime}\n</p>`, 4);
        AB.socketOut({ "name": "timer", "data": { "time": overallTime } });
    }
};

AB.world.endRun = function () {};
