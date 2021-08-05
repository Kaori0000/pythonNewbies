/*
 * jVector Maps
 */ 

var markers = 
[{ latLng: [41.50, -87.37], name: 'Chicago' }, 
{ latLng: [32.46, -96.46], name: 'Dallas' }, 
{ latLng: [36.10, -115.12], name: 'Las Vegas' }, 
{ latLng: [34.3, -118.15], name: 'Los Angeles' }, 
{ latLng: [40.43, -74.00], name: 'New York City' }, 
{ latLng: [53.412910, -8.243890], name: 'Ireland' }, 
{ latLng: [19.0760, 72.8777], name: 'Mumbai' }, 
{ latLng: [42.697708, 23.321868], name: 'Sofia, Bulgia' }, 
{ latLng: [40.014986, -105.270546], name: 'Boulder, CO' }];

$(function() {
    "use strict";
    var $jvectormapDiv = $('#jvectormap');
    if ($jvectormapDiv.length && $.fn.vectorMap) {
        $jvectormapDiv.vectorMap({
            map: 'world_mill',
            zoomOnScroll: false,
            hoverOpacity: 0.7,
            regionStyle: {
                initial: {
                    fill: '#e3ecff',
                    "fill-opacity": 1,
                    "stroke-width": 0,
                },
                hover: {
                    fill: '#cfdcf7',
                    "fill-opacity": 1,
                    cursor: 'pointer'
                },
            },
            markerStyle: {
                initial: {
                    fill: '#2761d8',
                    stroke: '#2761d8'
                }
            },
            markers: markers
        });
    }
});