camera = webcam;
nnet = alexnet;
while true
    picture = snapshot(camera);
    picture = imresize(picture,[227,227]);
    label = classify(nnet,picture);
    image(picture); 
    title(char(label));
    drawnow
end