let cvs = document.querySelector('Mirror');
let c = cvs.getContext('2d');

cvs.width = window.innerWidth;
cvs.height = window.innerHeight;

c.fillStyle='black';
c.fillRect(0,0,cvs.width,cvs.height);

/*var nunjucksRender = require('gulp-nunjucks-render');

gulp.task('nunjucks', function() {
    // Gets .html and .nunjucks files in pages
    return gulp.src('Thesis/pages/**.+(html|nunjucks)')
    // Renders template with nunjucks
    .pipe(nunjucksRender({
        path: ['Thesis/templates']
      }))
    // output files in Thesis folder
    .pipe(gulp.dest('Thesis'))
  });*/


