"use strict";(self["webpackChunkreborn_pokepedia"]=self["webpackChunkreborn_pokepedia"]||[]).push([[760],{8379:function(e,t,n){n.r(t),n.d(t,{createSwipeBackGesture:function(){return a}});var r=n(9185),o=n(3183),i=n(2635);
/*!
 * (C) Ionic http://ionicframework.com - MIT License
 */
const a=(e,t,n,a,c)=>{const s=e.ownerDocument.defaultView;let u=(0,o.i)(e);const d=e=>{const t=50,{startX:n}=e;return u?n>=s.innerWidth-t:n<=t},l=e=>u?-e.deltaX:e.deltaX,h=e=>u?-e.velocityX:e.velocityX,p=n=>(u=(0,o.i)(e),d(n)&&t()),k=e=>{const t=l(e),n=t/s.innerWidth;a(n)},b=e=>{const t=l(e),n=s.innerWidth,o=t/n,i=h(e),a=n/2,u=i>=0&&(i>.2||t>a),d=u?1-o:o,p=d*n;let k=0;if(p>5){const e=p/Math.abs(i);k=Math.min(e,540)}c(u,o<=0?.01:(0,r.m)(0,o,.9999),k)};return(0,i.createGesture)({el:e,gestureName:"goback-swipe",gesturePriority:101,threshold:10,canStart:p,onStart:n,onMove:k,onEnd:b})}}}]);
//# sourceMappingURL=760.c36bcf66.js.map