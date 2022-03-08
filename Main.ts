let cvs = <HTMLCanvasElement> document.querySelector('Mirror');
let c = cvs.getContext('2d');

cvs.width = window.innerWidth;
cvs.height = window.innerHeight;

c.fillStyle='black';
c.fillRect(0,0,cvs.width,cvs.height);
