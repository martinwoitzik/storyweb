from flask.ext.assets import Bundle

from storyweb.core import assets

js_assets = Bundle(
    'vendor/moment/moment.js',
    'vendor/angular/angular.js',
    'vendor/angular-route/angular-route.js',
    'vendor/angular-animate/angular-animate.js',
    'vendor/angular-contenteditable/angular-contenteditable.js',
    'vendor/angular-truncate/src/truncate.js',
    'vendor/angular-bootstrap/ui-bootstrap.js',
    'vendor/angular-bootstrap/ui-bootstrap-tpls.js',
    'vendor/angular-loading-bar/src/loading-bar.js',
    'js/app.js',
    'js/controllers/app.js',
    'js/controllers/article_list.js',
    'js/controllers/card.js',
    'js/controllers/card_new.js',
    'js/controllers/search.js',
    'js/directives/card_icon.js',
    'js/directives/card_item.js',
    'js/directives/link.js',
    'js/directives/pager.js',
    'js/directives/new_link.js',
    'js/directives/reference.js',
    filters='uglifyjs',
    output='assets/app.js'
)

css_assets = Bundle(
    'style/app.less',
    filters='less',
    output='assets/style.css'
)

assets.register('js', js_assets)
assets.register('css', css_assets)
