#!/bin/bash
# basic website template

#let script exit if a command fails

projectName=$1

if [[ -z $projectName ]]
then
    echo "enter an arguement in position one for new folder"
    set -o errexit 
fi

mkdir $projectName
cd $projectName

touch script.js
touch styles.css
touch index.html

# html template
echo "<!DOCTYPE html>" >> index.html
echo '<html lang="en">' >> index.html
echo "  <head>" >> index.html
echo '    <meta charset="utf-8"/>' >> index.html
echo "    <title> insert title here </title>" >> index.html
echo '    <link rel="stylesheet" type="text/css" href="./styles.css">' >> index.html
echo '    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">' >> index.html
echo "  </head>" >> index.html
echo "  <body>" >> index.html
echo '    <canvas id="myCanvas">' >> index.html
echo '    </canvas>' >> index.html
echo '    <script type="text/javascript" src="./script.js"></script>' >> index.html
echo '    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>' >> index.html
echo '    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>' >> index.html
echo '    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js" integrity="sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4" crossorigin="anonymous"></script>' >> index.html

echo "  </body>" >> index.html
echo '</html>' >> index.html


# light css template
echo "#myCanvas {" >> styles.css
echo "  margin: 0;" >> styles.css
echo "  /*input canvas styles here*/" >> styles.css
echo "}" >> styles.css
echo "/*make other styles as you want*/" >> styles.css

# js canvas template
echo '(function() {' >> script.js
echo '  var c = document.getElementById("myCanvas");' >> script.js
echo '  c.width = window.innerWidth;' >> script.js
echo '  c.height = window.innerHeight;' >> script.js
echo '  var ctx = c.getContext("2d");' >> script.js
echo '  ctx.font = "30px Arial";' >> script.js
echo '  ctx.fillText("Hello World", 10, 50);' >> script.js
echo '})();' >> script.js
