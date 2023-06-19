# CountyAmenitiesExplorer
Code for a website to serve, explore, and visualize US county natural amenities and cost of living.

The website will take a minute or two to load on initial visit, but will be quicker on subsequent loads

## Data Sources

To be added.

## To Build/Serve Locally

```
pip install shinylive

git clone https://github.com/j-andrews7/CountyAmenitiesExplorer.git
cd CountyAmenitiesExplorer

# To re-build static site.
shinylive export app docs

# To serve locally.
python3 -m http.server --directory docs --bind localhost 8008
```