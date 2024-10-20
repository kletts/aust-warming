
import * as d3 from "npm:d3";
import {svg, html} from "npm:htl"; 

export function bss_pal(newn) { 
    let bsspal = [ "#BDA14D",  "#3EBCB6", "#0169C4", "#153460",  "#D5114E", "#A56EB6",  "#4B1C57" ]; 
    let n = bsspal.length;
    if (newn <= n) { 
        return bsspal.slice(0, newn);
    } else { 
        let ncol = [ ...d3.range(0, 6, 6/(newn-1)), 6];
        let nint = ncol.map( d => d % 1);
        let nwhole = ncol.map( d => Math.floor(d));
        nwhole = nwhole.map((d, i) => d3.interpolate(bsspal[d], bsspal[d3.min([d+1, 6])])(nint[i]));
        return nwhole.map( d => d3.color(d).formatHex());
    }
} 

export function interpolate_palette(pal, newn) { 
    let n = pal.length -1; 
    let ncol = [ ...d3.range(0, n, n/(newn-1)), n];
    let nint = ncol.map( d => d % 1);
    let nwhole = ncol.map( d => Math.floor(d));
    nwhole = nwhole.map((d, i) => d3.interpolate(pal[d], pal[d3.min([d+1, n])])(nint[i]));
    return  nwhole.map( d => d3.color(d).formatHex());
}

export function swatches(colors, width=50) { 
    const n = colors.length;
    const w = width;  
    const dark = d3.lab(colors[0]).l < 50;;
    const canvas = svg`<svg viewBox="0 0 ${n} 1" style="display:block;width:${n * w}px;height:${w}px;margin:0 -14px;cursor:pointer;">${colors.map((c, i) => svg`<rect x=${i} width=1 height=1 fill=${c}>`)}`;
    return html`${canvas}`;
    }

export function lighten(colors, k=0.5) { 
    return d3.color(colors).copy({opacity: k})
    }

export function hex_to_rgb(pal) { 
    // removes opacity, returns array as required by deckgl
    return pal.map( d => Object.values(d3.rgb(d)).slice(0,-1)); 
    } 
