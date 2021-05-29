# jpeg-to-json

![jpegtojson](https://user-images.githubusercontent.com/79367505/120079901-c5d01600-c0be-11eb-96bb-feb6ae061afc.jpg)

Writes HEX color codes from jpeg into json.

# How this works?
You import a .jpeg/.jpg file and start the app. Then, you wait. Finnaly, you get a json file like this:

{1x1 : ffffff, 1x2 : 000000, 1x3 : fafafa, etc.}

# What does this mean?
{(X-pos of pixel)x(Y-pos of pixel) : #(hex-color code of the pixel)}

# Why?
Idk, maybe I will do a json-to-jpeg soon.
