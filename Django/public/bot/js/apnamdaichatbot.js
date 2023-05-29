//
//materialize.min.js
var _get=function t(e,i,n){null===e&&(e=Function.prototype);var s=Object.getOwnPropertyDescriptor(e,i);if(void 0===s){var o=Object.getPrototypeOf(e);return null===o?void 0:t(o,i,n)}if("value"in s)return s.value;var a=s.get;return void 0!==a?a.call(n):void 0},_createClass=function(){function n(t,e){for(var i=0;i<e.length;i++){var n=e[i];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(t,n.key,n)}}return function(t,e,i){return e&&n(t.prototype,e),i&&n(t,i),t}}();function _possibleConstructorReturn(t,e){if(!t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!e||"object"!=typeof e&&"function"!=typeof e?t:e}function _inherits(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function, not "+typeof e);t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,enumerable:!1,writable:!0,configurable:!0}}),e&&(Object.setPrototypeOf?Object.setPrototypeOf(t,e):t.__proto__=e)}function _classCallCheck(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}window.cash=function(){var i,o=document,a=window,t=Array.prototype,r=t.slice,n=t.filter,s=t.push,e=function(){},h=function(t){return typeof t==typeof e&&t.call},d=function(t){return"string"==typeof t},l=/^#[\w-]*$/,u=/^\.[\w-]*$/,c=/<.+>/,p=/^\w+$/;function v(t,e){e=e||o;var i=u.test(t)?e.getElementsByClassName(t.slice(1)):p.test(t)?e.getElementsByTagName(t):e.querySelectorAll(t);return i}function f(t){if(!i){var e=(i=o.implementation.createHTMLDocument(null)).createElement("base");e.href=o.location.href,i.head.appendChild(e)}return i.body.innerHTML=t,i.body.childNodes}function m(t){"loading"!==o.readyState?t():o.addEventListener("DOMContentLoaded",t)}function g(t,e){if(!t)return this;if(t.cash&&t!==a)return t;var i,n=t,s=0;if(d(t))n=l.test(t)?o.getElementById(t.slice(1)):c.test(t)?f(t):v(t,e);else if(h(t))return m(t),this;if(!n)return this;if(n.nodeType||n===a)this[0]=n,this.length=1;else for(i=this.length=n.length;s<i;s++)this[s]=n[s];return this}function _(t,e){return new g(t,e)}var y=_.fn=_.prototype=g.prototype={cash:!0,length:0,push:s,splice:t.splice,map:t.map,init:g};function k(t,e){for(var i=t.length,n=0;n<i&&!1!==e.call(t[n],t[n],n,t);n++);}function b(t,e){var i=t&&(t.matches||t.webkitMatchesSelector||t.mozMatchesSelector||t.msMatchesSelector||t.oMatchesSelector);return!!i&&i.call(t,e)}function w(e){return d(e)?b:e.cash?function(t){return e.is(t)}:function(t,e){return t===e}}function C(t){return _(r.call(t).filter(function(t,e,i){return i.indexOf(t)===e}))}Object.defineProperty(y,"constructor",{value:_}),_.parseHTML=f,_.noop=e,_.isFunction=h,_.isString=d,_.extend=y.extend=function(t){t=t||{};var e=r.call(arguments),i=e.length,n=1;for(1===e.length&&(t=this,n=0);n<i;n++)if(e[n])for(var s in e[n])e[n].hasOwnProperty(s)&&(t[s]=e[n][s]);return t},_.extend({merge:function(t,e){for(var i=+e.length,n=t.length,s=0;s<i;n++,s++)t[n]=e[s];return t.length=n,t},each:k,matches:b,unique:C,isArray:Array.isArray,isNumeric:function(t){return!isNaN(parseFloat(t))&&isFinite(t)}});var E=_.uid="_cash"+Date.now();function M(t){return t[E]=t[E]||{}}function O(t,e,i){return M(t)[e]=i}function x(t,e){var i=M(t);return void 0===i[e]&&(i[e]=t.dataset?t.dataset[e]:_(t).attr("data-"+e)),i[e]}y.extend({data:function(e,i){if(d(e))return void 0===i?x(this[0],e):this.each(function(t){return O(t,e,i)});for(var t in e)this.data(t,e[t]);return this},removeData:function(s){return this.each(function(t){return i=s,void((n=M(e=t))?delete n[i]:e.dataset?delete e.dataset[i]:_(e).removeAttr("data-"+name));var e,i,n})}});var L=/\S+/g;function T(t){return d(t)&&t.match(L)}function $(t,e){return t.classList?t.classList.contains(e):new RegExp("(^| )"+e+"( |$)","gi").test(t.className)}function B(t,e,i){t.classList?t.classList.add(e):i.indexOf(" "+e+" ")&&(t.className+=" "+e)}function D(t,e){t.classList?t.classList.remove(e):t.className=t.className.replace(e,"")}y.extend({addClass:function(t){var n=T(t);return n?this.each(function(e){var i=" "+e.className+" ";k(n,function(t){B(e,t,i)})}):this},attr:function(e,i){if(e){if(d(e))return void 0===i?this[0]?this[0].getAttribute?this[0].getAttribute(e):this[0][e]:void 0:this.each(function(t){t.setAttribute?t.setAttribute(e,i):t[e]=i});for(var t in e)this.attr(t,e[t]);return this}},hasClass:function(t){var e=!1,i=T(t);return i&&i.length&&this.each(function(t){return!(e=$(t,i[0]))}),e},prop:function(e,i){if(d(e))return void 0===i?this[0][e]:this.each(function(t){t[e]=i});for(var t in e)this.prop(t,e[t]);return this},removeAttr:function(e){return this.each(function(t){t.removeAttribute?t.removeAttribute(e):delete t[e]})},removeClass:function(t){if(!arguments.length)return this.attr("class","");var i=T(t);return i?this.each(function(e){k(i,function(t){D(e,t)})}):this},removeProp:function(e){return this.each(function(t){delete t[e]})},toggleClass:function(t,e){if(void 0!==e)return this[e?"addClass":"removeClass"](t);var n=T(t);return n?this.each(function(e){var i=" "+e.className+" ";k(n,function(t){$(e,t)?D(e,t):B(e,t,i)})}):this}}),y.extend({add:function(t,e){return C(_.merge(this,_(t,e)))},each:function(t){return k(this,t),this},eq:function(t){return _(this.get(t))},filter:function(e){if(!e)return this;var i=h(e)?e:w(e);return _(n.call(this,function(t){return i(t,e)}))},first:function(){return this.eq(0)},get:function(t){return void 0===t?r.call(this):t<0?this[t+this.length]:this[t]},index:function(t){var e=t?_(t)[0]:this[0],i=t?this:_(e).parent().children();return r.call(i).indexOf(e)},last:function(){return this.eq(-1)}});var S,I,A,R,H,P,W=(H=/(?:^\w|[A-Z]|\b\w)/g,P=/[\s-_]+/g,function(t){return t.replace(H,function(t,e){return t[0===e?"toLowerCase":"toUpperCase"]()}).replace(P,"")}),j=(S={},I=document,A=I.createElement("div"),R=A.style,function(e){if(e=W(e),S[e])return S[e];var t=e.charAt(0).toUpperCase()+e.slice(1),i=(e+" "+["webkit","moz","ms","o"].join(t+" ")+t).split(" ");return k(i,function(t){if(t in R)return S[t]=e=S[e]=t,!1}),S[e]});function F(t,e){return parseInt(a.getComputedStyle(t[0],null)[e],10)||0}function q(e,i,t){var n,s=x(e,"_cashEvents"),o=s&&s[i];o&&(t?(e.removeEventListener(i,t),0<=(n=o.indexOf(t))&&o.splice(n,1)):(k(o,function(t){e.removeEventListener(i,t)}),o=[]))}function N(t,e){return"&"+encodeURIComponent(t)+"="+encodeURIComponent(e).replace(/%20/g,"+")}function z(t){var e,i,n,s=t.type;if(!s)return null;switch(s.toLowerCase()){case"select-one":return 0<=(n=(i=t).selectedIndex)?i.options[n].value:null;case"select-multiple":return e=[],k(t.options,function(t){t.selected&&e.push(t.value)}),e.length?e:null;case"radio":case"checkbox":return t.checked?t.value:null;default:return t.value?t.value:null}}function V(e,i,n){var t=d(i);t||!i.length?k(e,t?function(t){return t.insertAdjacentHTML(n?"afterbegin":"beforeend",i)}:function(t,e){return function(t,e,i){if(i){var n=t.childNodes[0];t.insertBefore(e,n)}else t.appendChild(e)}(t,0===e?i:i.cloneNode(!0),n)}):k(i,function(t){return V(e,t,n)})}_.prefixedProp=j,_.camelCase=W,y.extend({css:function(e,i){if(d(e))return e=j(e),1<arguments.length?this.each(function(t){return t.style[e]=i}):a.getComputedStyle(this[0])[e];for(var t in e)this.css(t,e[t]);return this}}),k(["Width","Height"],function(e){var t=e.toLowerCase();y[t]=function(){return this[0].getBoundingClientRect()[t]},y["inner"+e]=function(){return this[0]["client"+e]},y["outer"+e]=function(t){return this[0]["offset"+e]+(t?F(this,"margin"+("Width"===e?"Left":"Top"))+F(this,"margin"+("Width"===e?"Right":"Bottom")):0)}}),y.extend({off:function(e,i){return this.each(function(t){return q(t,e,i)})},on:function(a,i,r,l){var n;if(!d(a)){for(var t in a)this.on(t,i,a[t]);return this}return h(i)&&(r=i,i=null),"ready"===a?(m(r),this):(i&&(n=r,r=function(t){for(var e=t.target;!b(e,i);){if(e===this||null===e)return e=!1;e=e.parentNode}e&&n.call(e,t)}),this.each(function(t){var e,i,n,s,o=r;l&&(o=function(){r.apply(this,arguments),q(t,a,o)}),i=a,n=o,(s=x(e=t,"_cashEvents")||O(e,"_cashEvents",{}))[i]=s[i]||[],s[i].push(n),e.addEventListener(i,n)}))},one:function(t,e,i){return this.on(t,e,i,!0)},ready:m,trigger:function(t,e){if(document.createEvent){var i=document.createEvent("HTMLEvents");return i.initEvent(t,!0,!1),i=this.extend(i,e),this.each(function(t){return t.dispatchEvent(i)})}}}),y.extend({serialize:function(){var s="";return k(this[0].elements||this,function(t){if(!t.disabled&&"FIELDSET"!==t.tagName){var e=t.name;switch(t.type.toLowerCase()){case"file":case"reset":case"submit":case"button":break;case"select-multiple":var i=z(t);null!==i&&k(i,function(t){s+=N(e,t)});break;default:var n=z(t);null!==n&&(s+=N(e,n))}}}),s.substr(1)},val:function(e){return void 0===e?z(this[0]):this.each(function(t){return t.value=e})}}),y.extend({after:function(t){return _(t).insertAfter(this),this},append:function(t){return V(this,t),this},appendTo:function(t){return V(_(t),this),this},before:function(t){return _(t).insertBefore(this),this},clone:function(){return _(this.map(function(t){return t.cloneNode(!0)}))},empty:function(){return this.html(""),this},html:function(t){if(void 0===t)return this[0].innerHTML;var e=t.nodeType?t[0].outerHTML:t;return this.each(function(t){return t.innerHTML=e})},insertAfter:function(t){var s=this;return _(t).each(function(t,e){var i=t.parentNode,n=t.nextSibling;s.each(function(t){i.insertBefore(0===e?t:t.cloneNode(!0),n)})}),this},insertBefore:function(t){var s=this;return _(t).each(function(e,i){var n=e.parentNode;s.each(function(t){n.insertBefore(0===i?t:t.cloneNode(!0),e)})}),this},prepend:function(t){return V(this,t,!0),this},prependTo:function(t){return V(_(t),this,!0),this},remove:function(){return this.each(function(t){if(t.parentNode)return t.parentNode.removeChild(t)})},text:function(e){return void 0===e?this[0].textContent:this.each(function(t){return t.textContent=e})}});var X=o.documentElement;return y.extend({position:function(){var t=this[0];return{left:t.offsetLeft,top:t.offsetTop}},offset:function(){var t=this[0].getBoundingClientRect();return{top:t.top+a.pageYOffset-X.clientTop,left:t.left+a.pageXOffset-X.clientLeft}},offsetParent:function(){return _(this[0].offsetParent)}}),y.extend({children:function(e){var i=[];return this.each(function(t){s.apply(i,t.children)}),i=C(i),e?i.filter(function(t){return b(t,e)}):i},closest:function(t){return!t||this.length<1?_():this.is(t)?this.filter(t):this.parent().closest(t)},is:function(e){if(!e)return!1;var i=!1,n=w(e);return this.each(function(t){return!(i=n(t,e))}),i},find:function(e){if(!e||e.nodeType)return _(e&&this.has(e).length?e:null);var i=[];return this.each(function(t){s.apply(i,v(e,t))}),C(i)},has:function(e){var t=d(e)?function(t){return 0!==v(e,t).length}:function(t){return t.contains(e)};return this.filter(t)},next:function(){return _(this[0].nextElementSibling)},not:function(e){if(!e)return this;var i=w(e);return this.filter(function(t){return!i(t,e)})},parent:function(){var e=[];return this.each(function(t){t&&t.parentNode&&e.push(t.parentNode)}),C(e)},parents:function(e){var i,n=[];return this.each(function(t){for(i=t;i&&i.parentNode&&i!==o.body.parentNode;)i=i.parentNode,(!e||e&&b(i,e))&&n.push(i)}),C(n)},prev:function(){return _(this[0].previousElementSibling)},siblings:function(t){var e=this.parent().children(t),i=this[0];return e.filter(function(t){return t!==i})}}),_}();var Component=function(){function s(t,e,i){_classCallCheck(this,s),e instanceof Element||console.error(Error(e+" is not an HTML Element"));var n=t.getInstance(e);n&&n.destroy(),this.el=e,this.$el=cash(e)}return _createClass(s,null,[{key:"init",value:function(t,e,i){var n=null;if(e instanceof Element)n=new t(e,i);else if(e&&(e.jquery||e.cash||e instanceof NodeList)){for(var s=[],o=0;o<e.length;o++)s.push(new t(e[o],i));n=s}return n}}]),s}();!function(t){t.Package?M={}:t.M={},M.jQueryLoaded=!!t.jQuery}(window),"function"==typeof define&&define.amd?define("M",[],function(){return M}):"undefined"==typeof exports||exports.nodeType||("undefined"!=typeof module&&!module.nodeType&&module.exports&&(exports=module.exports=M),exports.default=M),M.version="1.0.0",M.keys={TAB:9,ENTER:13,ESC:27,ARROW_UP:38,ARROW_DOWN:40},M.tabPressed=!1,M.keyDown=!1;var docHandleKeydown=function(t){M.keyDown=!0,t.which!==M.keys.TAB&&t.which!==M.keys.ARROW_DOWN&&t.which!==M.keys.ARROW_UP||(M.tabPressed=!0)},docHandleKeyup=function(t){M.keyDown=!1,t.which!==M.keys.TAB&&t.which!==M.keys.ARROW_DOWN&&t.which!==M.keys.ARROW_UP||(M.tabPressed=!1)},docHandleFocus=function(t){M.keyDown&&document.body.classList.add("keyboard-focused")},docHandleBlur=function(t){document.body.classList.remove("keyboard-focused")};document.addEventListener("keydown",docHandleKeydown,!0),document.addEventListener("keyup",docHandleKeyup,!0),document.addEventListener("focus",docHandleFocus,!0),document.addEventListener("blur",docHandleBlur,!0),M.initializeJqueryWrapper=function(n,s,o){jQuery.fn[s]=function(e){if(n.prototype[e]){var i=Array.prototype.slice.call(arguments,1);if("get"===e.slice(0,3)){var t=this.first()[0][o];return t[e].apply(t,i)}return this.each(function(){var t=this[o];t[e].apply(t,i)})}if("object"==typeof e||!e)return n.init(this,e),this;jQuery.error("Method "+e+" does not exist on jQuery."+s)}},M.AutoInit=function(t){var e=t||document.body,i={Autocomplete:e.querySelectorAll(".autocomplete:not(.no-autoinit)"),Carousel:e.querySelectorAll(".carousel:not(.no-autoinit)"),Chips:e.querySelectorAll(".chips:not(.no-autoinit)"),Collapsible:e.querySelectorAll(".collapsible:not(.no-autoinit)"),Datepicker:e.querySelectorAll(".datepicker:not(.no-autoinit)"),MyDropdown:e.querySelectorAll(".hqtdropdown-trigger:not(.no-autoinit)"),Materialbox:e.querySelectorAll(".materialboxed:not(.no-autoinit)"),Modal:e.querySelectorAll(".modal:not(.no-autoinit)"),Parallax:e.querySelectorAll(".parallax:not(.no-autoinit)"),Pushpin:e.querySelectorAll(".pushpin:not(.no-autoinit)"),ScrollSpy:e.querySelectorAll(".scrollspy:not(.no-autoinit)"),FormSelect:e.querySelectorAll("select:not(.no-autoinit)"),Sidenav:e.querySelectorAll(".sidenav:not(.no-autoinit)"),Tabs:e.querySelectorAll(".tabs:not(.no-autoinit)"),TapTarget:e.querySelectorAll(".tap-target:not(.no-autoinit)"),Timepicker:e.querySelectorAll(".timepicker:not(.no-autoinit)"),Tooltip:e.querySelectorAll(".tooltipped:not(.no-autoinit)"),FloatingActionButton:e.querySelectorAll(".fixed-action-btn:not(.no-autoinit)")};for(var n in i){M[n].init(i[n])}},M.objectSelectorString=function(t){return((t.prop("tagName")||"")+(t.attr("id")||"")+(t.attr("class")||"")).replace(/\s/g,"")},M.guid=function(){function t(){return Math.floor(65536*(1+Math.random())).toString(16).substring(1)}return function(){return t()+t()+"-"+t()+"-"+t()+"-"+t()+"-"+t()+t()+t()}}(),M.escapeHash=function(t){return t.replace(/(:|\.|\[|\]|,|=|\/)/g,"\\$1")},M.elementOrParentIsFixed=function(t){var e=$(t),i=e.add(e.parents()),n=!1;return i.each(function(){if("fixed"===$(this).css("position"))return!(n=!0)}),n},M.checkWithinContainer=function(t,e,i){var n={top:!1,right:!1,bottom:!1,left:!1},s=t.getBoundingClientRect(),o=t===document.body?Math.max(s.bottom,window.innerHeight):s.bottom,a=t.scrollLeft,r=t.scrollTop,l=e.left-a,h=e.top-r;return(l<s.left+i||l<i)&&(n.left=!0),(l+e.width>s.right-i||l+e.width>window.innerWidth-i)&&(n.right=!0),(h<s.top+i||h<i)&&(n.top=!0),(h+e.height>o-i||h+e.height>window.innerHeight-i)&&(n.bottom=!0),n},M.checkPossibleAlignments=function(t,e,i,n){var s={top:!0,right:!0,bottom:!0,left:!0,spaceOnTop:null,spaceOnRight:null,spaceOnBottom:null,spaceOnLeft:null},o="visible"===getComputedStyle(e).overflow,a=e.getBoundingClientRect(),r=Math.min(a.height,window.innerHeight),l=Math.min(a.width,window.innerWidth),h=t.getBoundingClientRect(),d=e.scrollLeft,u=e.scrollTop,c=i.left-d,p=i.top-u,v=i.top+h.height-u;return s.spaceOnRight=o?window.innerWidth-(h.left+i.width):l-(c+i.width),s.spaceOnRight<0&&(s.left=!1),s.spaceOnLeft=o?h.right-i.width:c-i.width+h.width,s.spaceOnLeft<0&&(s.right=!1),s.spaceOnBottom=o?window.innerHeight-(h.top+i.height+n):r-(p+i.height+n),s.spaceOnBottom<0&&(s.top=!1),s.spaceOnTop=o?h.bottom-(i.height+n):v-(i.height-n),s.spaceOnTop<0&&(s.bottom=!1),s},M.getOverflowParent=function(t){return null==t?null:t===document.body||"visible"!==getComputedStyle(t).overflow?t:M.getOverflowParent(t.parentElement)},M.getIdFromTrigger=function(t){var e=t.getAttribute("mydata-target");return e||(e=(e=t.getAttribute("href"))?e.slice(1):""),e},M.getDocumentScrollTop=function(){return window.pageYOffset||document.documentElement.scrollTop||document.body.scrollTop||0},M.getDocumentScrollLeft=function(){return window.pageXOffset||document.documentElement.scrollLeft||document.body.scrollLeft||0};var getTime=Date.now||function(){return(new Date).getTime()};M.throttle=function(i,n,s){var o=void 0,a=void 0,r=void 0,l=null,h=0;s||(s={});var d=function(){h=!1===s.leading?0:getTime(),l=null,r=i.apply(o,a),o=a=null};return function(){var t=getTime();h||!1!==s.leading||(h=t);var e=n-(t-h);return o=this,a=arguments,e<=0?(clearTimeout(l),l=null,h=t,r=i.apply(o,a),o=a=null):l||!1===s.trailing||(l=setTimeout(d,e)),r}};var $jscomp={scope:{}};$jscomp.defineProperty="function"==typeof Object.defineProperties?Object.defineProperty:function(t,e,i){if(i.get||i.set)throw new TypeError("ES3 does not support getters and setters.");t!=Array.prototype&&t!=Object.prototype&&(t[e]=i.value)},$jscomp.getGlobal=function(t){return"undefined"!=typeof window&&window===t?t:"undefined"!=typeof global&&null!=global?global:t},$jscomp.global=$jscomp.getGlobal(this),$jscomp.SYMBOL_PREFIX="jscomp_symbol_",$jscomp.initSymbol=function(){$jscomp.initSymbol=function(){},$jscomp.global.Symbol||($jscomp.global.Symbol=$jscomp.Symbol)},$jscomp.symbolCounter_=0,$jscomp.Symbol=function(t){return $jscomp.SYMBOL_PREFIX+(t||"")+$jscomp.symbolCounter_++},$jscomp.initSymbolIterator=function(){$jscomp.initSymbol();var t=$jscomp.global.Symbol.iterator;t||(t=$jscomp.global.Symbol.iterator=$jscomp.global.Symbol("iterator")),"function"!=typeof Array.prototype[t]&&$jscomp.defineProperty(Array.prototype,t,{configurable:!0,writable:!0,value:function(){return $jscomp.arrayIterator(this)}}),$jscomp.initSymbolIterator=function(){}},$jscomp.arrayIterator=function(t){var e=0;return $jscomp.iteratorPrototype(function(){return e<t.length?{done:!1,value:t[e++]}:{done:!0}})},$jscomp.iteratorPrototype=function(t){return $jscomp.initSymbolIterator(),(t={next:t})[$jscomp.global.Symbol.iterator]=function(){return this},t},$jscomp.array=$jscomp.array||{},$jscomp.iteratorFromArray=function(e,i){$jscomp.initSymbolIterator(),e instanceof String&&(e+="");var n=0,s={next:function(){if(n<e.length){var t=n++;return{value:i(t,e[t]),done:!1}}return s.next=function(){return{done:!0,value:void 0}},s.next()}};return s[Symbol.iterator]=function(){return s},s},$jscomp.polyfill=function(t,e,i,n){if(e){for(i=$jscomp.global,t=t.split("."),n=0;n<t.length-1;n++){var s=t[n];s in i||(i[s]={}),i=i[s]}(e=e(n=i[t=t[t.length-1]]))!=n&&null!=e&&$jscomp.defineProperty(i,t,{configurable:!0,writable:!0,value:e})}},$jscomp.polyfill("Array.prototype.keys",function(t){return t||function(){return $jscomp.iteratorFromArray(this,function(t){return t})}},"es6-impl","es3");var $jscomp$this=this;M.anime=function(){function s(t){if(!B.col(t))try{return document.querySelectorAll(t)}catch(t){}}function b(t,e){for(var i=t.length,n=2<=arguments.length?e:void 0,s=[],o=0;o<i;o++)if(o in t){var a=t[o];e.call(n,a,o,t)&&s.push(a)}return s}function d(t){return t.reduce(function(t,e){return t.concat(B.arr(e)?d(e):e)},[])}function o(t){return B.arr(t)?t:(B.str(t)&&(t=s(t)||t),t instanceof NodeList||t instanceof HTMLCollection?[].slice.call(t):[t])}function a(t,e){return t.some(function(t){return t===e})}function r(t){var e,i={};for(e in t)i[e]=t[e];return i}function u(t,e){var i,n=r(t);for(i in t)n[i]=e.hasOwnProperty(i)?e[i]:t[i];return n}function c(t,e){var i,n=r(t);for(i in e)n[i]=B.und(t[i])?e[i]:t[i];return n}function l(t){if(t=/([\+\-]?[0-9#\.]+)(%|px|pt|em|rem|in|cm|mm|ex|ch|pc|vw|vh|vmin|vmax|deg|rad|turn)?$/.exec(t))return t[2]}function h(t,e){return B.fnc(t)?t(e.target,e.id,e.total):t}function w(t,e){if(e in t.style)return getComputedStyle(t).getPropertyValue(e.replace(/([a-z])([A-Z])/g,"$1-$2").toLowerCase())||"0"}function p(t,e){return B.dom(t)&&a($,e)?"transform":B.dom(t)&&(t.getAttribute(e)||B.svg(t)&&t[e])?"attribute":B.dom(t)&&"transform"!==e&&w(t,e)?"css":null!=t[e]?"object":void 0}function v(t,e){switch(p(t,e)){case"transform":return function(t,i){var e,n=-1<(e=i).indexOf("translate")||"perspective"===e?"px":-1<e.indexOf("rotate")||-1<e.indexOf("skew")?"deg":void 0,n=-1<i.indexOf("scale")?1:0+n;if(!(t=t.style.transform))return n;for(var s=[],o=[],a=[],r=/(\w+)\((.+?)\)/g;s=r.exec(t);)o.push(s[1]),a.push(s[2]);return(t=b(a,function(t,e){return o[e]===i})).length?t[0]:n}(t,e);case"css":return w(t,e);case"attribute":return t.getAttribute(e)}return t[e]||0}function f(t,e){var i=/^(\*=|\+=|-=)/.exec(t);if(!i)return t;var n=l(t)||0;switch(e=parseFloat(e),t=parseFloat(t.replace(i[0],"")),i[0][0]){case"+":return e+t+n;case"-":return e-t+n;case"*":return e*t+n}}function m(t,e){return Math.sqrt(Math.pow(e.x-t.x,2)+Math.pow(e.y-t.y,2))}function i(t){t=t.points;for(var e,i=0,n=0;n<t.numberOfItems;n++){var s=t.getItem(n);0<n&&(i+=m(e,s)),e=s}return i}function g(t){if(t.getTotalLength)return t.getTotalLength();switch(t.tagName.toLowerCase()){case"circle":return 2*Math.PI*t.getAttribute("r");case"rect":return 2*t.getAttribute("width")+2*t.getAttribute("height");case"line":return m({x:t.getAttribute("x1"),y:t.getAttribute("y1")},{x:t.getAttribute("x2"),y:t.getAttribute("y2")});case"polyline":return i(t);case"polygon":var e=t.points;return i(t)+m(e.getItem(e.numberOfItems-1),e.getItem(0))}}function C(e,i){function t(t){return t=void 0===t?0:t,e.el.getPointAtLength(1<=i+t?i+t:0)}var n=t(),s=t(-1),o=t(1);switch(e.property){case"x":return n.x;case"y":return n.y;case"angle":return 180*Math.atan2(o.y-s.y,o.x-s.x)/Math.PI}}function _(t,e){var i,n=/-?\d*\.?\d+/g;if(i=B.pth(t)?t.totalLength:t,B.col(i))if(B.rgb(i)){var s=/rgb\((\d+,\s*[\d]+,\s*[\d]+)\)/g.exec(i);i=s?"rgba("+s[1]+",1)":i}else i=B.hex(i)?function(t){t=t.replace(/^#?([a-f\d])([a-f\d])([a-f\d])$/i,function(t,e,i,n){return e+e+i+i+n+n});var e=/^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(t);t=parseInt(e[1],16);var i=parseInt(e[2],16),e=parseInt(e[3],16);return"rgba("+t+","+i+","+e+",1)"}(i):B.hsl(i)?function(t){function e(t,e,i){return i<0&&(i+=1),1<i&&--i,i<1/6?t+6*(e-t)*i:i<.5?e:i<2/3?t+(e-t)*(2/3-i)*6:t}var i=/hsl\((\d+),\s*([\d.]+)%,\s*([\d.]+)%\)/g.exec(t)||/hsla\((\d+),\s*([\d.]+)%,\s*([\d.]+)%,\s*([\d.]+)\)/g.exec(t);t=parseInt(i[1])/360;var n=parseInt(i[2])/100,s=parseInt(i[3])/100,i=i[4]||1;if(0==n)s=n=t=s;else{var o=s<.5?s*(1+n):s+n-s*n,a=2*s-o,s=e(a,o,t+1/3),n=e(a,o,t);t=e(a,o,t-1/3)}return"rgba("+255*s+","+255*n+","+255*t+","+i+")"}(i):void 0;else s=(s=l(i))?i.substr(0,i.length-s.length):i,i=e&&!/\s/g.test(i)?s+e:s;return{original:i+="",numbers:i.match(n)?i.match(n).map(Number):[0],strings:B.str(t)||e?i.split(n):[]}}function y(t){return b(t=t?d(B.arr(t)?t.map(o):o(t)):[],function(t,e,i){return i.indexOf(t)===e})}function k(t,i){var e=r(i);if(B.arr(t)){var n=t.length;2!==n||B.obj(t[0])?B.fnc(i.duration)||(e.duration=i.duration/n):t={value:t}}return o(t).map(function(t,e){return e=e?0:i.delay,t=B.obj(t)&&!B.pth(t)?t:{value:t},B.und(t.delay)&&(t.delay=e),t}).map(function(t){return c(t,e)})}function E(o,a){var r;return o.tweens.map(function(t){var e=(t=function(t,e){var i,n={};for(i in t){var s=h(t[i],e);B.arr(s)&&1===(s=s.map(function(t){return h(t,e)})).length&&(s=s[0]),n[i]=s}return n.duration=parseFloat(n.duration),n.delay=parseFloat(n.delay),n}(t,a)).value,i=v(a.target,o.name),n=r?r.to.original:i,n=B.arr(e)?e[0]:n,s=f(B.arr(e)?e[1]:e,n),i=l(s)||l(n)||l(i);return t.from=_(n,i),t.to=_(s,i),t.start=r?r.end:o.offset,t.end=t.start+t.delay+t.duration,t.easing=function(t){return B.arr(t)?D.apply(this,t):S[t]}(t.easing),t.elasticity=(1e3-Math.min(Math.max(t.elasticity,1),999))/1e3,t.isPath=B.pth(e),t.isColor=B.col(t.from.original),t.isColor&&(t.round=1),r=t})}function M(e,t,i,n){var s="delay"===e;return t.length?(s?Math.min:Math.max).apply(Math,t.map(function(t){return t[e]})):s?n.delay:i.offset+n.delay+n.duration}function n(t){var e,i,n,s,o=u(L,t),a=u(T,t),r=(i=t.targets,(n=y(i)).map(function(t,e){return{target:t,id:e,total:n.length}})),l=[],h=c(o,a);for(e in t)h.hasOwnProperty(e)||"targets"===e||l.push({name:e,offset:h.offset,tweens:k(t[e],a)});return s=l,t=b(d(r.map(function(n){return s.map(function(t){var e=p(n.target,t.name);if(e){var i=E(t,n);t={type:e,property:t.name,animatable:n,tweens:i,duration:i[i.length-1].end,delay:i[0].delay}}else t=void 0;return t})})),function(t){return!B.und(t)}),c(o,{children:[],animatables:r,animations:t,duration:M("duration",t,o,a),delay:M("delay",t,o,a)})}function O(t){function d(){return window.Promise&&new Promise(function(t){return _=t})}function u(t){return k.reversed?k.duration-t:t}function c(e){for(var t=0,i={},n=k.animations,s=n.length;t<s;){var o=n[t],a=o.animatable,r=o.tweens,l=r.length-1,h=r[l];l&&(h=b(r,function(t){return e<t.end})[0]||h);for(var r=Math.min(Math.max(e-h.start-h.delay,0),h.duration)/h.duration,d=isNaN(r)?1:h.easing(r,h.elasticity),r=h.to.strings,u=h.round,l=[],c=void 0,c=h.to.numbers.length,p=0;p<c;p++){var v=void 0,v=h.to.numbers[p],f=h.from.numbers[p],v=h.isPath?C(h.value,d*v):f+d*(v-f);u&&(h.isColor&&2<p||(v=Math.round(v*u)/u)),l.push(v)}if(h=r.length)for(c=r[0],d=0;d<h;d++)u=r[d+1],p=l[d],isNaN(p)||(c=u?c+(p+u):c+(p+" "));else c=l[0];I[o.type](a.target,o.property,c,i,a.id),o.currentValue=c,t++}if(t=Object.keys(i).length)for(n=0;n<t;n++)x||(x=w(document.body,"transform")?"transform":"-webkit-transform"),k.animatables[n].target.style[x]=i[n].join(" ");k.currentTime=e,k.progress=e/k.duration*100}function p(t){k[t]&&k[t](k)}function v(){k.remaining&&!0!==k.remaining&&k.remaining--}function e(t){var e=k.duration,i=k.offset,n=i+k.delay,s=k.currentTime,o=k.reversed,a=u(t);if(k.children.length){var r=k.children,l=r.length;if(a>=k.currentTime)for(var h=0;h<l;h++)r[h].seek(a);else for(;l--;)r[l].seek(a)}(n<=a||!e)&&(k.began||(k.began=!0,p("begin")),p("run")),i<a&&a<e?c(a):(a<=i&&0!==s&&(c(0),o&&v()),(e<=a&&s!==e||!e)&&(c(e),o||v())),p("update"),e<=t&&(k.remaining?(m=f,"alternate"===k.direction&&(k.reversed=!k.reversed)):(k.pause(),k.completed||(k.completed=!0,p("complete"),"Promise"in window&&(_(),y=d()))),g=0)}t=void 0===t?{}:t;var f,m,g=0,_=null,y=d(),k=n(t);return k.reset=function(){var t=k.direction,e=k.loop;for(k.currentTime=0,k.progress=0,k.paused=!0,k.began=!1,k.completed=!1,k.reversed="reverse"===t,k.remaining="alternate"===t&&1===e?2:e,c(0),t=k.children.length;t--;)k.children[t].reset()},k.tick=function(t){f=t,m||(m=f),e((g+f-m)*O.speed)},k.seek=function(t){e(u(t))},k.pause=function(){var t=A.indexOf(k);-1<t&&A.splice(t,1),k.paused=!0},k.play=function(){k.paused&&(k.paused=!1,m=0,g=u(k.currentTime),A.push(k),R||H())},k.reverse=function(){k.reversed=!k.reversed,m=0,g=u(k.currentTime)},k.restart=function(){k.pause(),k.reset(),k.play()},k.finished=y,k.reset(),k.autoplay&&k.play(),k}var x,L={update:void 0,begin:void 0,run:void 0,complete:void 0,loop:1,direction:"normal",autoplay:!0,offset:0},T={duration:1e3,delay:0,easing:"easeOutElastic",elasticity:500,round:0},$="translateX translateY translateZ rotate rotateX rotateY rotateZ scale scaleX scaleY scaleZ skewX skewY perspective".split(" "),B={arr:function(t){return Array.isArray(t)},obj:function(t){return-1<Object.prototype.toString.call(t).indexOf("Object")},pth:function(t){return B.obj(t)&&t.hasOwnProperty("totalLength")},svg:function(t){return t instanceof SVGElement},dom:function(t){return t.nodeType||B.svg(t)},str:function(t){return"string"==typeof t},fnc:function(t){return"function"==typeof t},und:function(t){return void 0===t},hex:function(t){return/(^#[0-9A-F]{6}$)|(^#[0-9A-F]{3}$)/i.test(t)},rgb:function(t){return/^rgb/.test(t)},hsl:function(t){return/^hsl/.test(t)},col:function(t){return B.hex(t)||B.rgb(t)||B.hsl(t)}},D=function(){function u(t,e,i){return(((1-3*i+3*e)*t+(3*i-6*e))*t+3*e)*t}return function(a,r,l,h){if(0<=a&&a<=1&&0<=l&&l<=1){var d=new Float32Array(11);if(a!==r||l!==h)for(var t=0;t<11;++t)d[t]=u(.1*t,a,l);return function(t){if(a===r&&l===h)return t;if(0===t)return 0;if(1===t)return 1;for(var e=0,i=1;10!==i&&d[i]<=t;++i)e+=.1;var i=e+(t-d[--i])/(d[i+1]-d[i])*.1,n=3*(1-3*l+3*a)*i*i+2*(3*l-6*a)*i+3*a;if(.001<=n){for(e=0;e<4&&0!=(n=3*(1-3*l+3*a)*i*i+2*(3*l-6*a)*i+3*a);++e)var s=u(i,a,l)-t,i=i-s/n;t=i}else if(0===n)t=i;else{for(var i=e,e=e+.1,o=0;0<(n=u(s=i+(e-i)/2,a,l)-t)?e=s:i=s,1e-7<Math.abs(n)&&++o<10;);t=s}return u(t,r,h)}}}}(),S=function(){function i(t,e){return 0===t||1===t?t:-Math.pow(2,10*(t-1))*Math.sin(2*(t-1-e/(2*Math.PI)*Math.asin(1))*Math.PI/e)}var t,n="Quad Cubic Quart Quint Sine Expo Circ Back Elastic".split(" "),e={In:[[.55,.085,.68,.53],[.55,.055,.675,.19],[.895,.03,.685,.22],[.755,.05,.855,.06],[.47,0,.745,.715],[.95,.05,.795,.035],[.6,.04,.98,.335],[.6,-.28,.735,.045],i],Out:[[.25,.46,.45,.94],[.215,.61,.355,1],[.165,.84,.44,1],[.23,1,.32,1],[.39,.575,.565,1],[.19,1,.22,1],[.075,.82,.165,1],[.175,.885,.32,1.275],function(t,e){return 1-i(1-t,e)}],InOut:[[.455,.03,.515,.955],[.645,.045,.355,1],[.77,0,.175,1],[.86,0,.07,1],[.445,.05,.55,.95],[1,0,0,1],[.785,.135,.15,.86],[.68,-.55,.265,1.55],function(t,e){return t<.5?i(2*t,e)/2:1-i(-2*t+2,e)/2}]},s={linear:D(.25,.25,.75,.75)},o={};for(t in e)o.type=t,e[o.type].forEach(function(i){return function(t,e){s["ease"+i.type+n[e]]=B.fnc(t)?t:D.apply($jscomp$this,t)}}(o)),o={type:o.type};return s}(),I={css:function(t,e,i){return t.style[e]=i},attribute:function(t,e,i){return t.setAttribute(e,i)},object:function(t,e,i){return t[e]=i},transform:function(t,e,i,n,s){n[s]||(n[s]=[]),n[s].push(e+"("+i+")")}},A=[],R=0,H=function(){function n(){R=requestAnimationFrame(t)}function t(t){var e=A.length;if(e){for(var i=0;i<e;)A[i]&&A[i].tick(t),i++;n()}else cancelAnimationFrame(R),R=0}return n}();return O.version="2.2.0",O.speed=1,O.running=A,O.remove=function(t){t=y(t);for(var e=A.length;e--;)for(var i=A[e],n=i.animations,s=n.length;s--;)a(t,n[s].animatable.target)&&(n.splice(s,1),n.length||i.pause())},O.getValue=v,O.path=function(t,e){var i=B.str(t)?s(t)[0]:t,n=e||100;return function(t){return{el:i,property:t,totalLength:g(i)*(n/100)}}},O.setDashoffset=function(t){var e=g(t);return t.setAttribute("stroke-dasharray",e),e},O.bezier=D,O.easings=S,O.timeline=function(n){var s=O(n);return s.pause(),s.duration=0,s.add=function(t){return s.children.forEach(function(t){t.began=!0,t.completed=!0}),o(t).forEach(function(t){var e=c(t,u(T,n||{}));e.targets=e.targets||n.targets,t=s.duration;var i=e.offset;e.autoplay=!1,e.direction=s.direction,e.offset=B.und(i)?t:f(i,t),s.began=!0,s.completed=!0,s.seek(e.offset),(e=O(e)).began=!0,e.completed=!0,e.duration>t&&(s.duration=e.duration),s.children.push(e)}),s.seek(0),s.reset(),s.autoplay&&s.restart(),s},s},O.random=function(t,e){return Math.floor(Math.random()*(e-t+1))+t},O}(),function(r,l){"use strict";var e={accordion:!0,onOpenStart:void 0,onOpenEnd:void 0,onCloseStart:void 0,onCloseEnd:void 0,inDuration:300,outDuration:300},t=function(t){function s(t,e){_classCallCheck(this,s);var i=_possibleConstructorReturn(this,(s.__proto__||Object.getPrototypeOf(s)).call(this,s,t,e));(i.el.M_Collapsible=i).options=r.extend({},s.defaults,e),i.$headers=i.$el.children("li").children(".collapsible-header"),i.$headers.attr("tabindex",0),i._setupEventHandlers();var n=i.$el.children("li.active").children(".collapsible-body");return i.options.accordion?n.first().css("display","block"):n.css("display","block"),i}return _inherits(s,Component),_createClass(s,[{key:"destroy",value:function(){this._removeEventHandlers(),this.el.M_Collapsible=void 0}},{key:"_setupEventHandlers",value:function(){var e=this;this._handleCollapsibleClickBound=this._handleCollapsibleClick.bind(this),this._handleCollapsibleKeydownBound=this._handleCollapsibleKeydown.bind(this),this.el.addEventListener("click",this._handleCollapsibleClickBound),this.$headers.each(function(t){t.addEventListener("keydown",e._handleCollapsibleKeydownBound)})}},{key:"_removeEventHandlers",value:function(){var e=this;this.el.removeEventListener("click",this._handleCollapsibleClickBound),this.$headers.each(function(t){t.removeEventListener("keydown",e._handleCollapsibleKeydownBound)})}},{key:"_handleCollapsibleClick",value:function(t){var e=r(t.target).closest(".collapsible-header");if(t.target&&e.length){var i=e.closest(".collapsible");if(i[0]===this.el){var n=e.closest("li"),s=i.children("li"),o=n[0].classList.contains("active"),a=s.index(n);o?this.close(a):this.open(a)}}}},{key:"_handleCollapsibleKeydown",value:function(t){13===t.keyCode&&this._handleCollapsibleClickBound(t)}},{key:"_animateIn",value:function(t){var e=this,i=this.$el.children("li").eq(t);if(i.length){var n=i.children(".collapsible-body");l.remove(n[0]),n.css({display:"block",overflow:"hidden",height:0,paddingTop:"",paddingBottom:""});var s=n.css("padding-top"),o=n.css("padding-bottom"),a=n[0].scrollHeight;n.css({paddingTop:0,paddingBottom:0}),l({targets:n[0],height:a,paddingTop:s,paddingBottom:o,duration:this.options.inDuration,easing:"easeInOutCubic",complete:function(t){n.css({overflow:"",paddingTop:"",paddingBottom:"",height:""}),"function"==typeof e.options.onOpenEnd&&e.options.onOpenEnd.call(e,i[0])}})}}},{key:"_animateOut",value:function(t){var e=this,i=this.$el.children("li").eq(t);if(i.length){var n=i.children(".collapsible-body");l.remove(n[0]),n.css("overflow","hidden"),l({targets:n[0],height:0,paddingTop:0,paddingBottom:0,duration:this.options.outDuration,easing:"easeInOutCubic",complete:function(){n.css({height:"",overflow:"",padding:"",display:""}),"function"==typeof e.options.onCloseEnd&&e.options.onCloseEnd.call(e,i[0])}})}}},{key:"open",value:function(t){var i=this,e=this.$el.children("li").eq(t);if(e.length&&!e[0].classList.contains("active")){if("function"==typeof this.options.onOpenStart&&this.options.onOpenStart.call(this,e[0]),this.options.accordion){var n=this.$el.children("li");this.$el.children("li.active").each(function(t){var e=n.index(r(t));i.close(e)})}e[0].classList.add("active"),this._animateIn(t)}}},{key:"close",value:function(t){var e=this.$el.children("li").eq(t);e.length&&e[0].classList.contains("active")&&("function"==typeof this.options.onCloseStart&&this.options.onCloseStart.call(this,e[0]),e[0].classList.remove("active"),this._animateOut(t))}}],[{key:"init",value:function(t,e){return _get(s.__proto__||Object.getPrototypeOf(s),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Collapsible}},{key:"defaults",get:function(){return e}}]),s}();M.Collapsible=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"collapsible","M_Collapsible")}(cash,M.anime),function(h,i){"use strict";var e={alignment:"left",autoFocus:!0,constrainWidth:!0,container:null,coverTrigger:!0,closeOnClick:!0,hover:!1,inDuration:150,outDuration:250,onOpenStart:null,onOpenEnd:null,onCloseStart:null,onCloseEnd:null,onItemClick:null},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return i.el.M_MyDropdown=i,n._dropdowns.push(i),i.id=M.getIdFromTrigger(t),i.dropdownEl=document.getElementById(i.id),i.$dropdownEl=h(i.dropdownEl),i.options=h.extend({},n.defaults,e),i.isOpen=!1,i.isScrollable=!1,i.isTouchMoving=!1,i.focusedIndex=-1,i.filterQuery=[],i.options.container?h(i.options.container).append(i.dropdownEl):i.$el.after(i.dropdownEl),i._makeMyDropdownFocusable(),i._resetFilterQueryBound=i._resetFilterQuery.bind(i),i._handleDocumentClickBound=i._handleDocumentClick.bind(i),i._handleDocumentTouchmoveBound=i._handleDocumentTouchmove.bind(i),i._handleMyDropdownClickBound=i._handleMyDropdownClick.bind(i),i._handleMyDropdownKeydownBound=i._handleMyDropdownKeydown.bind(i),i._handleTriggerKeydownBound=i._handleTriggerKeydown.bind(i),i._setupEventHandlers(),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){this._resetMyDropdownStyles(),this._removeEventHandlers(),n._dropdowns.splice(n._dropdowns.indexOf(this),1),this.el.M_MyDropdown=void 0}},{key:"_setupEventHandlers",value:function(){this.el.addEventListener("keydown",this._handleTriggerKeydownBound),this.dropdownEl.addEventListener("click",this._handleMyDropdownClickBound),this.options.hover?(this._handleMouseEnterBound=this._handleMouseEnter.bind(this),this.el.addEventListener("mouseenter",this._handleMouseEnterBound),this._handleMouseLeaveBound=this._handleMouseLeave.bind(this),this.el.addEventListener("mouseleave",this._handleMouseLeaveBound),this.dropdownEl.addEventListener("mouseleave",this._handleMouseLeaveBound)):(this._handleClickBound=this._handleClick.bind(this),this.el.addEventListener("click",this._handleClickBound))}},{key:"_removeEventHandlers",value:function(){this.el.removeEventListener("keydown",this._handleTriggerKeydownBound),this.dropdownEl.removeEventListener("click",this._handleMyDropdownClickBound),this.options.hover?(this.el.removeEventListener("mouseenter",this._handleMouseEnterBound),this.el.removeEventListener("mouseleave",this._handleMouseLeaveBound),this.dropdownEl.removeEventListener("mouseleave",this._handleMouseLeaveBound)):this.el.removeEventListener("click",this._handleClickBound)}},{key:"_setupTemporaryEventHandlers",value:function(){document.body.addEventListener("click",this._handleDocumentClickBound,!0),document.body.addEventListener("touchend",this._handleDocumentClickBound),document.body.addEventListener("touchmove",this._handleDocumentTouchmoveBound),this.dropdownEl.addEventListener("keydown",this._handleMyDropdownKeydownBound)}},{key:"_removeTemporaryEventHandlers",value:function(){document.body.removeEventListener("click",this._handleDocumentClickBound,!0),document.body.removeEventListener("touchend",this._handleDocumentClickBound),document.body.removeEventListener("touchmove",this._handleDocumentTouchmoveBound),this.dropdownEl.removeEventListener("keydown",this._handleMyDropdownKeydownBound)}},{key:"_handleClick",value:function(t){t.preventDefault(),this.open()}},{key:"_handleMouseEnter",value:function(){this.open()}},{key:"_handleMouseLeave",value:function(t){var e=t.toElement||t.relatedTarget,i=!!h(e).closest("#hqtdropdown").length,n=!1,s=h(e).closest(".hqtdropdown-trigger");s.length&&s[0].M_MyDropdown&&s[0].M_MyDropdown.isOpen&&(n=!0),n||i||this.close()}},{key:"_handleDocumentClick",value:function(t){var e=this,i=h(t.target);this.options.closeOnClick&&i.closest("#hqtdropdown").length&&!this.isTouchMoving?setTimeout(function(){e.close()},0):!i.closest(".hqtdropdown-trigger").length&&i.closest("#hqtdropdown").length||setTimeout(function(){e.close()},0),this.isTouchMoving=!1}},{key:"_handleTriggerKeydown",value:function(t){t.which!==M.keys.ARROW_DOWN&&t.which!==M.keys.ENTER||this.isOpen||(t.preventDefault(),this.open())}},{key:"_handleDocumentTouchmove",value:function(t){h(t.target).closest("#hqtdropdown").length&&(this.isTouchMoving=!0)}},{key:"_handleMyDropdownClick",value:function(t){if("function"==typeof this.options.onItemClick){var e=h(t.target).closest("li")[0];this.options.onItemClick.call(this,e)}}},{key:"_handleMyDropdownKeydown",value:function(t){if(t.which===M.keys.TAB)t.preventDefault(),this.close();else if(t.which!==M.keys.ARROW_DOWN&&t.which!==M.keys.ARROW_UP||!this.isOpen)if(t.which===M.keys.ENTER&&this.isOpen){var e=this.dropdownEl.children[this.focusedIndex],i=h(e).find("a, button").first();i.length?i[0].click():e&&e.click()}else t.which===M.keys.ESC&&this.isOpen&&(t.preventDefault(),this.close());else{t.preventDefault();var n=t.which===M.keys.ARROW_DOWN?1:-1,s=this.focusedIndex,o=!1;do{if(s+=n,this.dropdownEl.children[s]&&-1!==this.dropdownEl.children[s].tabIndex){o=!0;break}}while(s<this.dropdownEl.children.length&&0<=s);o&&(this.focusedIndex=s,this._focusFocusedItem())}var a=String.fromCharCode(t.which).toLowerCase();if(a&&-1===[9,13,27,38,40].indexOf(t.which)){this.filterQuery.push(a);var r=this.filterQuery.join(""),l=h(this.dropdownEl).find("li").filter(function(t){return 0===h(t).text().toLowerCase().indexOf(r)})[0];l&&(this.focusedIndex=h(l).index(),this._focusFocusedItem())}this.filterTimeout=setTimeout(this._resetFilterQueryBound,1e3)}},{key:"_resetFilterQuery",value:function(){this.filterQuery=[]}},{key:"_resetMyDropdownStyles",value:function(){this.$dropdownEl.css({display:"",width:"",height:"",left:"",top:"","transform-origin":"",transform:"",opacity:""})}},{key:"_makeMyDropdownFocusable",value:function(){this.dropdownEl.tabIndex=0,h(this.dropdownEl).children().each(function(t){t.getAttribute("tabindex")||t.setAttribute("tabindex",0)})}},{key:"_focusFocusedItem",value:function(){0<=this.focusedIndex&&this.focusedIndex<this.dropdownEl.children.length&&this.options.autoFocus&&this.dropdownEl.children[this.focusedIndex].focus()}},{key:"_getMyDropdownPosition",value:function(){this.el.offsetParent.getBoundingClientRect();var t=this.el.getBoundingClientRect(),e=this.dropdownEl.getBoundingClientRect(),i=e.height,n=e.width,s=t.left-e.left,o=t.top-e.top,a={left:s,top:o,height:i,width:n},r=this.dropdownEl.offsetParent?this.dropdownEl.offsetParent:this.dropdownEl.parentNode,l=M.checkPossibleAlignments(this.el,r,a,this.options.coverTrigger?0:t.height),h="top",d=this.options.alignment;if(o+=this.options.coverTrigger?0:t.height,this.isScrollable=!1,l.top||(l.bottom?h="bottom":(this.isScrollable=!0,l.spaceOnTop>l.spaceOnBottom?(h="bottom",i+=l.spaceOnTop,o-=l.spaceOnTop):i+=l.spaceOnBottom)),!l[d]){var u="left"===d?"right":"left";l[u]?d=u:l.spaceOnLeft>l.spaceOnRight?(d="right",n+=l.spaceOnLeft,s-=l.spaceOnLeft):(d="left",n+=l.spaceOnRight)}return"bottom"===h&&(o=o-e.height+(this.options.coverTrigger?t.height:0)),"right"===d&&(s=s-e.width+t.width),{x:s,y:o,verticalAlignment:h,horizontalAlignment:d,height:i,width:n}}},{key:"_animateIn",value:function(){var e=this;i.remove(this.dropdownEl),i({targets:this.dropdownEl,opacity:{value:[0,1],easing:"easeOutQuad"},scaleX:[.3,1],scaleY:[.3,1],duration:this.options.inDuration,easing:"easeOutQuint",complete:function(t){e.options.autoFocus&&e.dropdownEl.focus(),"function"==typeof e.options.onOpenEnd&&e.options.onOpenEnd.call(e,e.el)}})}},{key:"_animateOut",value:function(){var e=this;i.remove(this.dropdownEl),i({targets:this.dropdownEl,opacity:{value:0,easing:"easeOutQuint"},scaleX:.3,scaleY:.3,duration:this.options.outDuration,easing:"easeOutQuint",complete:function(t){e._resetMyDropdownStyles(),"function"==typeof e.options.onCloseEnd&&e.options.onCloseEnd.call(e,e.el)}})}},{key:"_placeMyDropdown",value:function(){var t=this.options.constrainWidth?this.el.getBoundingClientRect().width:this.dropdownEl.getBoundingClientRect().width;this.dropdownEl.style.width=t+"px";var e=this._getMyDropdownPosition();this.dropdownEl.style.left=e.x+"px",this.dropdownEl.style.top=e.y+"px",this.dropdownEl.style.height=e.height+"px",this.dropdownEl.style.width=e.width+"px",this.dropdownEl.style.transformOrigin=("left"===e.horizontalAlignment?"0":"100%")+" "+("top"===e.verticalAlignment?"0":"100%")}},{key:"open",value:function(){this.isOpen||(this.isOpen=!0,"function"==typeof this.options.onOpenStart&&this.options.onOpenStart.call(this,this.el),this._resetMyDropdownStyles(),this.dropdownEl.style.display="block",this._placeMyDropdown(),this._animateIn(),this._setupTemporaryEventHandlers())}},{key:"close",value:function(){this.isOpen&&(this.isOpen=!1,this.focusedIndex=-1,"function"==typeof this.options.onCloseStart&&this.options.onCloseStart.call(this,this.el),this._animateOut(),this._removeTemporaryEventHandlers(),this.options.autoFocus&&this.el.focus())}},{key:"recalculateDimensions",value:function(){this.isOpen&&(this.$dropdownEl.css({width:"",height:"",left:"",top:"","transform-origin":""}),this._placeMyDropdown())}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_MyDropdown}},{key:"defaults",get:function(){return e}}]),n}();t._dropdowns=[],M.MyDropdown=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"dropdown","M_MyDropdown")}(cash,M.anime),function(s,i){"use strict";var e={opacity:.5,inDuration:250,outDuration:250,onOpenStart:null,onOpenEnd:null,onCloseStart:null,onCloseEnd:null,preventScrolling:!0,dismissible:!0,startingTop:"4%",endingTop:"10%"},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return(i.el.M_Modal=i).options=s.extend({},n.defaults,e),i.isOpen=!1,i.id=i.$el.attr("id"),i._openingTrigger=void 0,i.$overlay=s('<div class="modal-overlay"></div>'),i.el.tabIndex=0,i._nthModalOpened=0,n._count++,i._setupEventHandlers(),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){n._count--,this._removeEventHandlers(),this.el.removeAttribute("style"),this.$overlay.remove(),this.el.M_Modal=void 0}},{key:"_setupEventHandlers",value:function(){this._handleOverlayClickBound=this._handleOverlayClick.bind(this),this._handleModalCloseClickBound=this._handleModalCloseClick.bind(this),1===n._count&&document.body.addEventListener("click",this._handleTriggerClick),this.$overlay[0].addEventListener("click",this._handleOverlayClickBound),this.el.addEventListener("click",this._handleModalCloseClickBound)}},{key:"_removeEventHandlers",value:function(){0===n._count&&document.body.removeEventListener("click",this._handleTriggerClick),this.$overlay[0].removeEventListener("click",this._handleOverlayClickBound),this.el.removeEventListener("click",this._handleModalCloseClickBound)}},{key:"_handleTriggerClick",value:function(t){var e=s(t.target).closest(".modal-trigger");if(e.length){var i=M.getIdFromTrigger(e[0]),n=document.getElementById(i).M_Modal;n&&n.open(e),t.preventDefault()}}},{key:"_handleOverlayClick",value:function(){this.options.dismissible&&this.close()}},{key:"_handleModalCloseClick",value:function(t){s(t.target).closest(".modal-close").length&&this.close()}},{key:"_handleKeydown",value:function(t){27===t.keyCode&&this.options.dismissible&&this.close()}},{key:"_handleFocus",value:function(t){this.el.contains(t.target)||this._nthModalOpened!==n._modalsOpen||this.el.focus()}},{key:"_animateIn",value:function(){var t=this;s.extend(this.el.style,{display:"block",opacity:0}),s.extend(this.$overlay[0].style,{display:"block",opacity:0}),i({targets:this.$overlay[0],opacity:this.options.opacity,duration:this.options.inDuration,easing:"easeOutQuad"});var e={targets:this.el,duration:this.options.inDuration,easing:"easeOutCubic",complete:function(){"function"==typeof t.options.onOpenEnd&&t.options.onOpenEnd.call(t,t.el,t._openingTrigger)}};this.el.classList.contains("bottom-sheet")?s.extend(e,{bottom:0,opacity:1}):s.extend(e,{top:[this.options.startingTop,this.options.endingTop],opacity:1,scaleX:[.8,1],scaleY:[.8,1]}),i(e)}},{key:"_animateOut",value:function(){var t=this;i({targets:this.$overlay[0],opacity:0,duration:this.options.outDuration,easing:"easeOutQuart"});var e={targets:this.el,duration:this.options.outDuration,easing:"easeOutCubic",complete:function(){t.el.style.display="none",t.$overlay.remove(),"function"==typeof t.options.onCloseEnd&&t.options.onCloseEnd.call(t,t.el)}};this.el.classList.contains("bottom-sheet")?s.extend(e,{bottom:"-100%",opacity:0}):s.extend(e,{top:[this.options.endingTop,this.options.startingTop],opacity:0,scaleX:.8,scaleY:.8}),i(e)}},{key:"open",value:function(t){if(!this.isOpen)return this.isOpen=!0,n._modalsOpen++,this._nthModalOpened=n._modalsOpen,this.$overlay[0].style.zIndex=1e3+2*n._modalsOpen,this.el.style.zIndex=1e3+2*n._modalsOpen+1,this._openingTrigger=t?t[0]:void 0,"function"==typeof this.options.onOpenStart&&this.options.onOpenStart.call(this,this.el,this._openingTrigger),this.options.preventScrolling&&(document.body.style.overflow="hidden"),this.el.classList.add("open"),this.el.insertAdjacentElement("afterend",this.$overlay[0]),this.options.dismissible&&(this._handleKeydownBound=this._handleKeydown.bind(this),this._handleFocusBound=this._handleFocus.bind(this),document.addEventListener("keydown",this._handleKeydownBound),document.addEventListener("focus",this._handleFocusBound,!0)),i.remove(this.el),i.remove(this.$overlay[0]),this._animateIn(),this.el.focus(),this}},{key:"close",value:function(){if(this.isOpen)return this.isOpen=!1,n._modalsOpen--,this._nthModalOpened=0,"function"==typeof this.options.onCloseStart&&this.options.onCloseStart.call(this,this.el),this.el.classList.remove("open"),0===n._modalsOpen&&(document.body.style.overflow=""),this.options.dismissible&&(document.removeEventListener("keydown",this._handleKeydownBound),document.removeEventListener("focus",this._handleFocusBound,!0)),i.remove(this.el),i.remove(this.$overlay[0]),this._animateOut(),this}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Modal}},{key:"defaults",get:function(){return e}}]),n}();t._modalsOpen=0,t._count=0,M.Modal=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"modal","M_Modal")}(cash,M.anime),function(o,a){"use strict";var e={inDuration:275,outDuration:200,onOpenStart:null,onOpenEnd:null,onCloseStart:null,onCloseEnd:null},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return(i.el.M_Materialbox=i).options=o.extend({},n.defaults,e),i.overlayActive=!1,i.doneAnimating=!0,i.placeholder=o("<div></div>").addClass("material-placeholder"),i.originalWidth=0,i.originalHeight=0,i.originInlineStyles=i.$el.attr("style"),i.caption=i.el.getAttribute("data-caption")||"",i.$el.before(i.placeholder),i.placeholder.append(i.$el),i._setupEventHandlers(),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){this._removeEventHandlers(),this.el.M_Materialbox=void 0,o(this.placeholder).after(this.el).remove(),this.$el.removeAttr("style")}},{key:"_setupEventHandlers",value:function(){this._handleMaterialboxClickBound=this._handleMaterialboxClick.bind(this),this.el.addEventListener("click",this._handleMaterialboxClickBound)}},{key:"_removeEventHandlers",value:function(){this.el.removeEventListener("click",this._handleMaterialboxClickBound)}},{key:"_handleMaterialboxClick",value:function(t){!1===this.doneAnimating||this.overlayActive&&this.doneAnimating?this.close():this.open()}},{key:"_handleWindowScroll",value:function(){this.overlayActive&&this.close()}},{key:"_handleWindowResize",value:function(){this.overlayActive&&this.close()}},{key:"_handleWindowEscape",value:function(t){27===t.keyCode&&this.doneAnimating&&this.overlayActive&&this.close()}},{key:"_makeAncestorsOverflowVisible",value:function(){this.ancestorsChanged=o();for(var t=this.placeholder[0].parentNode;null!==t&&!o(t).is(document);){var e=o(t);"visible"!==e.css("overflow")&&(e.css("overflow","visible"),void 0===this.ancestorsChanged?this.ancestorsChanged=e:this.ancestorsChanged=this.ancestorsChanged.add(e)),t=t.parentNode}}},{key:"_animateImageIn",value:function(){var t=this,e={targets:this.el,height:[this.originalHeight,this.newHeight],width:[this.originalWidth,this.newWidth],left:M.getDocumentScrollLeft()+this.windowWidth/2-this.placeholder.offset().left-this.newWidth/2,top:M.getDocumentScrollTop()+this.windowHeight/2-this.placeholder.offset().top-this.newHeight/2,duration:this.options.inDuration,easing:"easeOutQuad",complete:function(){t.doneAnimating=!0,"function"==typeof t.options.onOpenEnd&&t.options.onOpenEnd.call(t,t.el)}};this.maxWidth=this.$el.css("max-width"),this.maxHeight=this.$el.css("max-height"),"none"!==this.maxWidth&&(e.maxWidth=this.newWidth),"none"!==this.maxHeight&&(e.maxHeight=this.newHeight),a(e)}},{key:"_animateImageOut",value:function(){var t=this,e={targets:this.el,width:this.originalWidth,height:this.originalHeight,left:0,top:0,duration:this.options.outDuration,easing:"easeOutQuad",complete:function(){t.placeholder.css({height:"",width:"",position:"",top:"",left:""}),t.attrWidth&&t.$el.attr("width",t.attrWidth),t.attrHeight&&t.$el.attr("height",t.attrHeight),t.$el.removeAttr("style"),t.originInlineStyles&&t.$el.attr("style",t.originInlineStyles),t.$el.removeClass("active"),t.doneAnimating=!0,t.ancestorsChanged.length&&t.ancestorsChanged.css("overflow",""),"function"==typeof t.options.onCloseEnd&&t.options.onCloseEnd.call(t,t.el)}};a(e)}},{key:"_updateVars",value:function(){this.windowWidth=window.innerWidth,this.windowHeight=window.innerHeight,this.caption=this.el.getAttribute("data-caption")||""}},{key:"open",value:function(){var t=this;this._updateVars(),this.originalWidth=this.el.getBoundingClientRect().width,this.originalHeight=this.el.getBoundingClientRect().height,this.doneAnimating=!1,this.$el.addClass("active"),this.overlayActive=!0,"function"==typeof this.options.onOpenStart&&this.options.onOpenStart.call(this,this.el),this.placeholder.css({width:this.placeholder[0].getBoundingClientRect().width+"px",height:this.placeholder[0].getBoundingClientRect().height+"px",position:"relative",top:0,left:0}),this._makeAncestorsOverflowVisible(),this.$el.css({position:"absolute","z-index":1e3,"will-change":"left, top, width, height"}),this.attrWidth=this.$el.attr("width"),this.attrHeight=this.$el.attr("height"),this.attrWidth&&(this.$el.css("width",this.attrWidth+"px"),this.$el.removeAttr("width")),this.attrHeight&&(this.$el.css("width",this.attrHeight+"px"),this.$el.removeAttr("height")),this.$overlay=o('<div id="materialbox-overlay"></div>').css({opacity:0}).one("click",function(){t.doneAnimating&&t.close()}),this.$el.before(this.$overlay);var e=this.$overlay[0].getBoundingClientRect();this.$overlay.css({width:this.windowWidth+"px",height:this.windowHeight+"px",left:-1*e.left+"px",top:-1*e.top+"px"}),a.remove(this.el),a.remove(this.$overlay[0]),a({targets:this.$overlay[0],opacity:1,duration:this.options.inDuration,easing:"easeOutQuad"}),""!==this.caption&&(this.$photocaption&&a.remove(this.$photoCaption[0]),this.$photoCaption=o('<div class="materialbox-caption"></div>'),this.$photoCaption.text(this.caption),o("body").append(this.$photoCaption),this.$photoCaption.css({display:"inline"}),a({targets:this.$photoCaption[0],opacity:1,duration:this.options.inDuration,easing:"easeOutQuad"}));var i=0,n=this.originalWidth/this.windowWidth,s=this.originalHeight/this.windowHeight;this.newWidth=0,this.newHeight=0,s<n?(i=this.originalHeight/this.originalWidth,this.newWidth=.9*this.windowWidth,this.newHeight=.9*this.windowWidth*i):(i=this.originalWidth/this.originalHeight,this.newWidth=.9*this.windowHeight*i,this.newHeight=.9*this.windowHeight),this._animateImageIn(),this._handleWindowScrollBound=this._handleWindowScroll.bind(this),this._handleWindowResizeBound=this._handleWindowResize.bind(this),this._handleWindowEscapeBound=this._handleWindowEscape.bind(this),window.addEventListener("scroll",this._handleWindowScrollBound),window.addEventListener("resize",this._handleWindowResizeBound),window.addEventListener("keyup",this._handleWindowEscapeBound)}},{key:"close",value:function(){var t=this;this._updateVars(),this.doneAnimating=!1,"function"==typeof this.options.onCloseStart&&this.options.onCloseStart.call(this,this.el),a.remove(this.el),a.remove(this.$overlay[0]),""!==this.caption&&a.remove(this.$photoCaption[0]),window.removeEventListener("scroll",this._handleWindowScrollBound),window.removeEventListener("resize",this._handleWindowResizeBound),window.removeEventListener("keyup",this._handleWindowEscapeBound),a({targets:this.$overlay[0],opacity:0,duration:this.options.outDuration,easing:"easeOutQuad",complete:function(){t.overlayActive=!1,t.$overlay.remove()}}),this._animateImageOut(),""!==this.caption&&a({targets:this.$photoCaption[0],opacity:0,duration:this.options.outDuration,easing:"easeOutQuad",complete:function(){t.$photoCaption.remove()}})}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Materialbox}},{key:"defaults",get:function(){return e}}]),n}();M.Materialbox=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"materialbox","M_Materialbox")}(cash,M.anime),function(s){"use strict";var e={responsiveThreshold:0},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return(i.el.M_Parallax=i).options=s.extend({},n.defaults,e),i._enabled=window.innerWidth>i.options.responsiveThreshold,i.$img=i.$el.find("img").first(),i.$img.each(function(){this.complete&&s(this).trigger("load")}),i._updateParallax(),i._setupEventHandlers(),i._setupStyles(),n._parallaxes.push(i),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){n._parallaxes.splice(n._parallaxes.indexOf(this),1),this.$img[0].style.transform="",this._removeEventHandlers(),this.$el[0].M_Parallax=void 0}},{key:"_setupEventHandlers",value:function(){this._handleImageLoadBound=this._handleImageLoad.bind(this),this.$img[0].addEventListener("load",this._handleImageLoadBound),0===n._parallaxes.length&&(n._handleScrollThrottled=M.throttle(n._handleScroll,5),window.addEventListener("scroll",n._handleScrollThrottled),n._handleWindowResizeThrottled=M.throttle(n._handleWindowResize,5),window.addEventListener("resize",n._handleWindowResizeThrottled))}},{key:"_removeEventHandlers",value:function(){this.$img[0].removeEventListener("load",this._handleImageLoadBound),0===n._parallaxes.length&&(window.removeEventListener("scroll",n._handleScrollThrottled),window.removeEventListener("resize",n._handleWindowResizeThrottled))}},{key:"_setupStyles",value:function(){this.$img[0].style.opacity=1}},{key:"_handleImageLoad",value:function(){this._updateParallax()}},{key:"_updateParallax",value:function(){var t=0<this.$el.height()?this.el.parentNode.offsetHeight:500,e=this.$img[0].offsetHeight-t,i=this.$el.offset().top+t,n=this.$el.offset().top,s=M.getDocumentScrollTop(),o=window.innerHeight,a=e*((s+o-n)/(t+o));this._enabled?s<i&&n<s+o&&(this.$img[0].style.transform="translate3D(-50%, "+a+"px, 0)"):this.$img[0].style.transform=""}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Parallax}},{key:"_handleScroll",value:function(){for(var t=0;t<n._parallaxes.length;t++){var e=n._parallaxes[t];e._updateParallax.call(e)}}},{key:"_handleWindowResize",value:function(){for(var t=0;t<n._parallaxes.length;t++){var e=n._parallaxes[t];e._enabled=window.innerWidth>e.options.responsiveThreshold}}},{key:"defaults",get:function(){return e}}]),n}();t._parallaxes=[],M.Parallax=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"parallax","M_Parallax")}(cash),function(a,s){"use strict";var e={duration:300,onShow:null,swipeable:!1,responsiveThreshold:1/0},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return(i.el.M_Tabs=i).options=a.extend({},n.defaults,e),i.$tabLinks=i.$el.children("li.tab").children("a"),i.index=0,i._setupActiveTabLink(),i.options.swipeable?i._setupSwipeableTabs():i._setupNormalTabs(),i._setTabsAndTabWidth(),i._createIndicator(),i._setupEventHandlers(),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){this._removeEventHandlers(),this._indicator.parentNode.removeChild(this._indicator),this.options.swipeable?this._teardownSwipeableTabs():this._teardownNormalTabs(),this.$el[0].M_Tabs=void 0}},{key:"_setupEventHandlers",value:function(){this._handleWindowResizeBound=this._handleWindowResize.bind(this),window.addEventListener("resize",this._handleWindowResizeBound),this._handleTabClickBound=this._handleTabClick.bind(this),this.el.addEventListener("click",this._handleTabClickBound)}},{key:"_removeEventHandlers",value:function(){window.removeEventListener("resize",this._handleWindowResizeBound),this.el.removeEventListener("click",this._handleTabClickBound)}},{key:"_handleWindowResize",value:function(){this._setTabsAndTabWidth(),0!==this.tabWidth&&0!==this.tabsWidth&&(this._indicator.style.left=this._calcLeftPos(this.$activeTabLink)+"px",this._indicator.style.right=this._calcRightPos(this.$activeTabLink)+"px")}},{key:"_handleTabClick",value:function(t){var e=this,i=a(t.target).closest("li.tab"),n=a(t.target).closest("a");if(n.length&&n.parent().hasClass("tab"))if(i.hasClass("disabled"))t.preventDefault();else if(!n.attr("target")){this.$activeTabLink.removeClass("active");var s=this.$content;this.$activeTabLink=n,this.$content=a(M.escapeHash(n[0].hash)),this.$tabLinks=this.$el.children("li.tab").children("a"),this.$activeTabLink.addClass("active");var o=this.index;this.index=Math.max(this.$tabLinks.index(n),0),this.options.swipeable?this._tabsCarousel&&this._tabsCarousel.set(this.index,function(){"function"==typeof e.options.onShow&&e.options.onShow.call(e,e.$content[0])}):this.$content.length&&(this.$content[0].style.display="block",this.$content.addClass("active"),"function"==typeof this.options.onShow&&this.options.onShow.call(this,this.$content[0]),s.length&&!s.is(this.$content)&&(s[0].style.display="none",s.removeClass("active"))),this._setTabsAndTabWidth(),this._animateIndicator(o),t.preventDefault()}}},{key:"_createIndicator",value:function(){var t=this,e=document.createElement("li");e.classList.add("indicator"),this.el.appendChild(e),this._indicator=e,setTimeout(function(){t._indicator.style.left=t._calcLeftPos(t.$activeTabLink)+"px",t._indicator.style.right=t._calcRightPos(t.$activeTabLink)+"px"},0)}},{key:"_setupActiveTabLink",value:function(){this.$activeTabLink=a(this.$tabLinks.filter('[href="'+location.hash+'"]')),0===this.$activeTabLink.length&&(this.$activeTabLink=this.$el.children("li.tab").children("a.active").first()),0===this.$activeTabLink.length&&(this.$activeTabLink=this.$el.children("li.tab").children("a").first()),this.$tabLinks.removeClass("active"),this.$activeTabLink[0].classList.add("active"),this.index=Math.max(this.$tabLinks.index(this.$activeTabLink),0),this.$activeTabLink.length&&(this.$content=a(M.escapeHash(this.$activeTabLink[0].hash)),this.$content.addClass("active"))}},{key:"_setupSwipeableTabs",value:function(){var i=this;window.innerWidth>this.options.responsiveThreshold&&(this.options.swipeable=!1);var n=a();this.$tabLinks.each(function(t){var e=a(M.escapeHash(t.hash));e.addClass("carousel-item"),n=n.add(e)});var t=a('<div class="tabs-content carousel carousel-slider"></div>');n.first().before(t),t.append(n),n[0].style.display="";var e=this.$activeTabLink.closest(".tab").index();this._tabsCarousel=M.Carousel.init(t[0],{fullWidth:!0,noWrap:!0,onCycleTo:function(t){var e=i.index;i.index=a(t).index(),i.$activeTabLink.removeClass("active"),i.$activeTabLink=i.$tabLinks.eq(i.index),i.$activeTabLink.addClass("active"),i._animateIndicator(e),"function"==typeof i.options.onShow&&i.options.onShow.call(i,i.$content[0])}}),this._tabsCarousel.set(e)}},{key:"_teardownSwipeableTabs",value:function(){var t=this._tabsCarousel.$el;this._tabsCarousel.destroy(),t.after(t.children()),t.remove()}},{key:"_setupNormalTabs",value:function(){this.$tabLinks.not(this.$activeTabLink).each(function(t){if(t.hash){var e=a(M.escapeHash(t.hash));e.length&&(e[0].style.display="none")}})}},{key:"_teardownNormalTabs",value:function(){this.$tabLinks.each(function(t){if(t.hash){var e=a(M.escapeHash(t.hash));e.length&&(e[0].style.display="")}})}},{key:"_setTabsAndTabWidth",value:function(){this.tabsWidth=this.$el.width(),this.tabWidth=Math.max(this.tabsWidth,this.el.scrollWidth)/this.$tabLinks.length}},{key:"_calcRightPos",value:function(t){return Math.ceil(this.tabsWidth-t.position().left-t[0].getBoundingClientRect().width)}},{key:"_calcLeftPos",value:function(t){return Math.floor(t.position().left)}},{key:"updateTabIndicator",value:function(){this._setTabsAndTabWidth(),this._animateIndicator(this.index)}},{key:"_animateIndicator",value:function(t){var e=0,i=0;0<=this.index-t?e=90:i=90;var n={targets:this._indicator,left:{value:this._calcLeftPos(this.$activeTabLink),delay:e},right:{value:this._calcRightPos(this.$activeTabLink),delay:i},duration:this.options.duration,easing:"easeOutQuad"};s.remove(this._indicator),s(n)}},{key:"select",value:function(t){var e=this.$tabLinks.filter('[href="#'+t+'"]');e.length&&e.trigger("click")}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Tabs}},{key:"defaults",get:function(){return e}}]),n}();M.Tabs=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"tabs","M_Tabs")}(cash,M.anime),function(d,e){"use strict";var i={exitDelay:200,enterDelay:0,html:null,margin:5,inDuration:250,outDuration:200,position:"bottom",transitionMovement:10},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return(i.el.M_Tooltip=i).options=d.extend({},n.defaults,e),i.isOpen=!1,i.isHovered=!1,i.isFocused=!1,i._appendTooltipEl(),i._setupEventHandlers(),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){d(this.tooltipEl).remove(),this._removeEventHandlers(),this.el.M_Tooltip=void 0}},{key:"_appendTooltipEl",value:function(){var t=document.createElement("div");t.classList.add("material-tooltip"),this.tooltipEl=t;var e=document.createElement("div");e.classList.add("tooltip-content"),e.innerHTML=this.options.html,t.appendChild(e),document.body.appendChild(t)}},{key:"_updateTooltipContent",value:function(){this.tooltipEl.querySelector(".tooltip-content").innerHTML=this.options.html}},{key:"_setupEventHandlers",value:function(){this._handleMouseEnterBound=this._handleMouseEnter.bind(this),this._handleMouseLeaveBound=this._handleMouseLeave.bind(this),this._handleFocusBound=this._handleFocus.bind(this),this._handleBlurBound=this._handleBlur.bind(this),this.el.addEventListener("mouseenter",this._handleMouseEnterBound),this.el.addEventListener("mouseleave",this._handleMouseLeaveBound),this.el.addEventListener("focus",this._handleFocusBound,!0),this.el.addEventListener("blur",this._handleBlurBound,!0)}},{key:"_removeEventHandlers",value:function(){this.el.removeEventListener("mouseenter",this._handleMouseEnterBound),this.el.removeEventListener("mouseleave",this._handleMouseLeaveBound),this.el.removeEventListener("focus",this._handleFocusBound,!0),this.el.removeEventListener("blur",this._handleBlurBound,!0)}},{key:"open",value:function(t){this.isOpen||(t=void 0===t||void 0,this.isOpen=!0,this.options=d.extend({},this.options,this._getAttributeOptions()),this._updateTooltipContent(),this._setEnterDelayTimeout(t))}},{key:"close",value:function(){this.isOpen&&(this.isHovered=!1,this.isFocused=!1,this.isOpen=!1,this._setExitDelayTimeout())}},{key:"_setExitDelayTimeout",value:function(){var t=this;clearTimeout(this._exitDelayTimeout),this._exitDelayTimeout=setTimeout(function(){t.isHovered||t.isFocused||t._animateOut()},this.options.exitDelay)}},{key:"_setEnterDelayTimeout",value:function(t){var e=this;clearTimeout(this._enterDelayTimeout),this._enterDelayTimeout=setTimeout(function(){(e.isHovered||e.isFocused||t)&&e._animateIn()},this.options.enterDelay)}},{key:"_positionTooltip",value:function(){var t,e=this.el,i=this.tooltipEl,n=e.offsetHeight,s=e.offsetWidth,o=i.offsetHeight,a=i.offsetWidth,r=this.options.margin,l=void 0,h=void 0;this.xMovement=0,this.yMovement=0,l=e.getBoundingClientRect().top+M.getDocumentScrollTop(),h=e.getBoundingClientRect().left+M.getDocumentScrollLeft(),"top"===this.options.position?(l+=-o-r,h+=s/2-a/2,this.yMovement=-this.options.transitionMovement):"right"===this.options.position?(l+=n/2-o/2,h+=s+r,this.xMovement=this.options.transitionMovement):"left"===this.options.position?(l+=n/2-o/2,h+=-a-r,this.xMovement=-this.options.transitionMovement):(l+=n+r,h+=s/2-a/2,this.yMovement=this.options.transitionMovement),t=this._repositionWithinScreen(h,l,a,o),d(i).css({top:t.y+"px",left:t.x+"px"})}},{key:"_repositionWithinScreen",value:function(t,e,i,n){var s=M.getDocumentScrollLeft(),o=M.getDocumentScrollTop(),a=t-s,r=e-o,l={left:a,top:r,width:i,height:n},h=this.options.margin+this.options.transitionMovement,d=M.checkWithinContainer(document.body,l,h);return d.left?a=h:d.right&&(a-=a+i-window.innerWidth),d.top?r=h:d.bottom&&(r-=r+n-window.innerHeight),{x:a+s,y:r+o}}},{key:"_animateIn",value:function(){this._positionTooltip(),this.tooltipEl.style.visibility="visible",e.remove(this.tooltipEl),e({targets:this.tooltipEl,opacity:1,translateX:this.xMovement,translateY:this.yMovement,duration:this.options.inDuration,easing:"easeOutCubic"})}},{key:"_animateOut",value:function(){e.remove(this.tooltipEl),e({targets:this.tooltipEl,opacity:0,translateX:0,translateY:0,duration:this.options.outDuration,easing:"easeOutCubic"})}},{key:"_handleMouseEnter",value:function(){this.isHovered=!0,this.isFocused=!1,this.open(!1)}},{key:"_handleMouseLeave",value:function(){this.isHovered=!1,this.isFocused=!1,this.close()}},{key:"_handleFocus",value:function(){M.tabPressed&&(this.isFocused=!0,this.open(!1))}},{key:"_handleBlur",value:function(){this.isFocused=!1,this.close()}},{key:"_getAttributeOptions",value:function(){var t={},e=this.el.getAttribute("data-tooltip"),i=this.el.getAttribute("data-position");return e&&(t.html=e),i&&(t.position=i),t}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Tooltip}},{key:"defaults",get:function(){return i}}]),n}();M.Tooltip=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"tooltip","M_Tooltip")}(cash,M.anime),function(i){"use strict";var t=t||{},e=document.querySelectorAll.bind(document);function m(t){var e="";for(var i in t)t.hasOwnProperty(i)&&(e+=i+":"+t[i]+";");return e}var g={duration:750,show:function(t,e){if(2===t.button)return!1;var i=e||this,n=document.createElement("div");n.className="waves-ripple",i.appendChild(n);var s,o,a,r,l,h,d,u=(h={top:0,left:0},d=(s=i)&&s.ownerDocument,o=d.documentElement,void 0!==s.getBoundingClientRect&&(h=s.getBoundingClientRect()),a=null!==(l=r=d)&&l===l.window?r:9===r.nodeType&&r.defaultView,{top:h.top+a.pageYOffset-o.clientTop,left:h.left+a.pageXOffset-o.clientLeft}),c=t.pageY-u.top,p=t.pageX-u.left,v="scale("+i.clientWidth/100*10+")";"touches"in t&&(c=t.touches[0].pageY-u.top,p=t.touches[0].pageX-u.left),n.setAttribute("data-hold",Date.now()),n.setAttribute("data-scale",v),n.setAttribute("data-x",p),n.setAttribute("data-y",c);var f={top:c+"px",left:p+"px"};n.className=n.className+" waves-notransition",n.setAttribute("style",m(f)),n.className=n.className.replace("waves-notransition",""),f["-webkit-transform"]=v,f["-moz-transform"]=v,f["-ms-transform"]=v,f["-o-transform"]=v,f.transform=v,f.opacity="1",f["-webkit-transition-duration"]=g.duration+"ms",f["-moz-transition-duration"]=g.duration+"ms",f["-o-transition-duration"]=g.duration+"ms",f["transition-duration"]=g.duration+"ms",f["-webkit-transition-timing-function"]="cubic-bezier(0.250, 0.460, 0.450, 0.940)",f["-moz-transition-timing-function"]="cubic-bezier(0.250, 0.460, 0.450, 0.940)",f["-o-transition-timing-function"]="cubic-bezier(0.250, 0.460, 0.450, 0.940)",f["transition-timing-function"]="cubic-bezier(0.250, 0.460, 0.450, 0.940)",n.setAttribute("style",m(f))},hide:function(t){l.touchup(t);var e=this,i=(e.clientWidth,null),n=e.getElementsByClassName("waves-ripple");if(!(0<n.length))return!1;var s=(i=n[n.length-1]).getAttribute("data-x"),o=i.getAttribute("data-y"),a=i.getAttribute("data-scale"),r=350-(Date.now()-Number(i.getAttribute("data-hold")));r<0&&(r=0),setTimeout(function(){var t={top:o+"px",left:s+"px",opacity:"0","-webkit-transition-duration":g.duration+"ms","-moz-transition-duration":g.duration+"ms","-o-transition-duration":g.duration+"ms","transition-duration":g.duration+"ms","-webkit-transform":a,"-moz-transform":a,"-ms-transform":a,"-o-transform":a,transform:a};i.setAttribute("style",m(t)),setTimeout(function(){try{e.removeChild(i)}catch(t){return!1}},g.duration)},r)},wrapInput:function(t){for(var e=0;e<t.length;e++){var i=t[e];if("input"===i.tagName.toLowerCase()){var n=i.parentNode;if("i"===n.tagName.toLowerCase()&&-1!==n.className.indexOf("waves-effect"))continue;var s=document.createElement("i");s.className=i.className+" waves-input-wrapper";var o=i.getAttribute("style");o||(o=""),s.setAttribute("style",o),i.className="waves-button-input",i.removeAttribute("style"),n.replaceChild(s,i),s.appendChild(i)}}}},l={touches:0,allowEvent:function(t){var e=!0;return"touchstart"===t.type?l.touches+=1:"touchend"===t.type||"touchcancel"===t.type?setTimeout(function(){0<l.touches&&(l.touches-=1)},500):"mousedown"===t.type&&0<l.touches&&(e=!1),e},touchup:function(t){l.allowEvent(t)}};function n(t){var e=function(t){if(!1===l.allowEvent(t))return null;for(var e=null,i=t.target||t.srcElement;null!==i.parentNode;){if(!(i instanceof SVGElement)&&-1!==i.className.indexOf("waves-effect")){e=i;break}i=i.parentNode}return e}(t);null!==e&&(g.show(t,e),"ontouchstart"in i&&(e.addEventListener("touchend",g.hide,!1),e.addEventListener("touchcancel",g.hide,!1)),e.addEventListener("mouseup",g.hide,!1),e.addEventListener("mouseleave",g.hide,!1),e.addEventListener("dragend",g.hide,!1))}t.displayEffect=function(t){"duration"in(t=t||{})&&(g.duration=t.duration),g.wrapInput(e(".waves-effect")),"ontouchstart"in i&&document.body.addEventListener("touchstart",n,!1),document.body.addEventListener("mousedown",n,!1)},t.attach=function(t){"input"===t.tagName.toLowerCase()&&(g.wrapInput([t]),t=t.parentNode),"ontouchstart"in i&&t.addEventListener("touchstart",n,!1),t.addEventListener("mousedown",n,!1)},i.Waves=t,document.addEventListener("DOMContentLoaded",function(){t.displayEffect()},!1)}(window),function(i,n){"use strict";var t={html:"",displayLength:4e3,inDuration:300,outDuration:375,classes:"",completeCallback:null,activationPercent:.8},e=function(){function s(t){_classCallCheck(this,s),this.options=i.extend({},s.defaults,t),this.message=this.options.html,this.panning=!1,this.timeRemaining=this.options.displayLength,0===s._toasts.length&&s._createContainer(),s._toasts.push(this);var e=this._createToast();(e.M_Toast=this).el=e,this.$el=i(e),this._animateIn(),this._setTimer()}return _createClass(s,[{key:"_createToast",value:function(){var t=document.createElement("div");return t.classList.add("toast"),this.options.classes.length&&i(t).addClass(this.options.classes),("object"==typeof HTMLElement?this.message instanceof HTMLElement:this.message&&"object"==typeof this.message&&null!==this.message&&1===this.message.nodeType&&"string"==typeof this.message.nodeName)?t.appendChild(this.message):this.message.jquery?i(t).append(this.message[0]):t.innerHTML=this.message,s._container.appendChild(t),t}},{key:"_animateIn",value:function(){n({targets:this.el,top:0,opacity:1,duration:this.options.inDuration,easing:"easeOutCubic"})}},{key:"_setTimer",value:function(){var t=this;this.timeRemaining!==1/0&&(this.counterInterval=setInterval(function(){t.panning||(t.timeRemaining-=20),t.timeRemaining<=0&&t.dismiss()},20))}},{key:"dismiss",value:function(){var t=this;window.clearInterval(this.counterInterval);var e=this.el.offsetWidth*this.options.activationPercent;this.wasSwiped&&(this.el.style.transition="transform .05s, opacity .05s",this.el.style.transform="translateX("+e+"px)",this.el.style.opacity=0),n({targets:this.el,opacity:0,marginTop:-40,duration:this.options.outDuration,easing:"easeOutExpo",complete:function(){"function"==typeof t.options.completeCallback&&t.options.completeCallback(),t.$el.remove(),s._toasts.splice(s._toasts.indexOf(t),1),0===s._toasts.length&&s._removeContainer()}})}}],[{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Toast}},{key:"_createContainer",value:function(){var t=document.createElement("div");t.setAttribute("id","toast-container"),t.addEventListener("touchstart",s._onDragStart),t.addEventListener("touchmove",s._onDragMove),t.addEventListener("touchend",s._onDragEnd),t.addEventListener("mousedown",s._onDragStart),document.addEventListener("mousemove",s._onDragMove),document.addEventListener("mouseup",s._onDragEnd),document.body.appendChild(t),s._container=t}},{key:"_removeContainer",value:function(){document.removeEventListener("mousemove",s._onDragMove),document.removeEventListener("mouseup",s._onDragEnd),i(s._container).remove(),s._container=null}},{key:"_onDragStart",value:function(t){if(t.target&&i(t.target).closest(".toast").length){var e=i(t.target).closest(".toast")[0].M_Toast;e.panning=!0,(s._draggedToast=e).el.classList.add("panning"),e.el.style.transition="",e.startingXPos=s._xPos(t),e.time=Date.now(),e.xPos=s._xPos(t)}}},{key:"_onDragMove",value:function(t){if(s._draggedToast){t.preventDefault();var e=s._draggedToast;e.deltaX=Math.abs(e.xPos-s._xPos(t)),e.xPos=s._xPos(t),e.velocityX=e.deltaX/(Date.now()-e.time),e.time=Date.now();var i=e.xPos-e.startingXPos,n=e.el.offsetWidth*e.options.activationPercent;e.el.style.transform="translateX("+i+"px)",e.el.style.opacity=1-Math.abs(i/n)}}},{key:"_onDragEnd",value:function(){if(s._draggedToast){var t=s._draggedToast;t.panning=!1,t.el.classList.remove("panning");var e=t.xPos-t.startingXPos,i=t.el.offsetWidth*t.options.activationPercent;Math.abs(e)>i||1<t.velocityX?(t.wasSwiped=!0,t.dismiss()):(t.el.style.transition="transform .2s, opacity .2s",t.el.style.transform="",t.el.style.opacity=""),s._draggedToast=null}}},{key:"_xPos",value:function(t){return t.targetTouches&&1<=t.targetTouches.length?t.targetTouches[0].clientX:t.clientX}},{key:"dismissAll",value:function(){for(var t in s._toasts)s._toasts[t].dismiss()}},{key:"defaults",get:function(){return t}}]),s}();e._toasts=[],e._container=null,e._draggedToast=null,M.Toast=e,M.toast=function(t){return new e(t)}}(cash,M.anime),function(s,o){"use strict";var e={edge:"left",draggable:!0,inDuration:250,outDuration:200,onOpenStart:null,onOpenEnd:null,onCloseStart:null,onCloseEnd:null,preventScrolling:!0},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return(i.el.M_Sidenav=i).id=i.$el.attr("id"),i.options=s.extend({},n.defaults,e),i.isOpen=!1,i.isFixed=i.el.classList.contains("sidenav-fixed"),i.isDragged=!1,i.lastWindowWidth=window.innerWidth,i.lastWindowHeight=window.innerHeight,i._createOverlay(),i._createDragTarget(),i._setupEventHandlers(),i._setupClasses(),i._setupFixed(),n._sidenavs.push(i),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){this._removeEventHandlers(),this._enableBodyScrolling(),this._overlay.parentNode.removeChild(this._overlay),this.dragTarget.parentNode.removeChild(this.dragTarget),this.el.M_Sidenav=void 0,this.el.style.transform="";var t=n._sidenavs.indexOf(this);0<=t&&n._sidenavs.splice(t,1)}},{key:"_createOverlay",value:function(){var t=document.createElement("div");this._closeBound=this.close.bind(this),t.classList.add("sidenav-overlay"),t.addEventListener("click",this._closeBound),document.body.appendChild(t),this._overlay=t}},{key:"_setupEventHandlers",value:function(){0===n._sidenavs.length&&document.body.addEventListener("click",this._handleTriggerClick),this._handleDragTargetDragBound=this._handleDragTargetDrag.bind(this),this._handleDragTargetReleaseBound=this._handleDragTargetRelease.bind(this),this._handleCloseDragBound=this._handleCloseDrag.bind(this),this._handleCloseReleaseBound=this._handleCloseRelease.bind(this),this._handleCloseTriggerClickBound=this._handleCloseTriggerClick.bind(this),this.dragTarget.addEventListener("touchmove",this._handleDragTargetDragBound),this.dragTarget.addEventListener("touchend",this._handleDragTargetReleaseBound),this._overlay.addEventListener("touchmove",this._handleCloseDragBound),this._overlay.addEventListener("touchend",this._handleCloseReleaseBound),this.el.addEventListener("touchmove",this._handleCloseDragBound),this.el.addEventListener("touchend",this._handleCloseReleaseBound),this.el.addEventListener("click",this._handleCloseTriggerClickBound),this.isFixed&&(this._handleWindowResizeBound=this._handleWindowResize.bind(this),window.addEventListener("resize",this._handleWindowResizeBound))}},{key:"_removeEventHandlers",value:function(){1===n._sidenavs.length&&document.body.removeEventListener("click",this._handleTriggerClick),this.dragTarget.removeEventListener("touchmove",this._handleDragTargetDragBound),this.dragTarget.removeEventListener("touchend",this._handleDragTargetReleaseBound),this._overlay.removeEventListener("touchmove",this._handleCloseDragBound),this._overlay.removeEventListener("touchend",this._handleCloseReleaseBound),this.el.removeEventListener("touchmove",this._handleCloseDragBound),this.el.removeEventListener("touchend",this._handleCloseReleaseBound),this.el.removeEventListener("click",this._handleCloseTriggerClickBound),this.isFixed&&window.removeEventListener("resize",this._handleWindowResizeBound)}},{key:"_handleTriggerClick",value:function(t){var e=s(t.target).closest(".sidenav-trigger");if(t.target&&e.length){var i=M.getIdFromTrigger(e[0]),n=document.getElementById(i).M_Sidenav;n&&n.open(e),t.preventDefault()}}},{key:"_startDrag",value:function(t){var e=t.targetTouches[0].clientX;this.isDragged=!0,this._startingXpos=e,this._xPos=this._startingXpos,this._time=Date.now(),this._width=this.el.getBoundingClientRect().width,this._overlay.style.display="block",this._initialScrollTop=this.isOpen?this.el.scrollTop:M.getDocumentScrollTop(),this._verticallyScrolling=!1,o.remove(this.el),o.remove(this._overlay)}},{key:"_dragMoveUpdate",value:function(t){var e=t.targetTouches[0].clientX,i=this.isOpen?this.el.scrollTop:M.getDocumentScrollTop();this.deltaX=Math.abs(this._xPos-e),this._xPos=e,this.velocityX=this.deltaX/(Date.now()-this._time),this._time=Date.now(),this._initialScrollTop!==i&&(this._verticallyScrolling=!0)}},{key:"_handleDragTargetDrag",value:function(t){if(this.options.draggable&&!this._isCurrentlyFixed()&&!this._verticallyScrolling){this.isDragged||this._startDrag(t),this._dragMoveUpdate(t);var e=this._xPos-this._startingXpos,i=0<e?"right":"left";e=Math.min(this._width,Math.abs(e)),this.options.edge===i&&(e=0);var n=e,s="translateX(-100%)";"right"===this.options.edge&&(s="translateX(100%)",n=-n),this.percentOpen=Math.min(1,e/this._width),this.el.style.transform=s+" translateX("+n+"px)",this._overlay.style.opacity=this.percentOpen}}},{key:"_handleDragTargetRelease",value:function(){this.isDragged&&(.2<this.percentOpen?this.open():this._animateOut(),this.isDragged=!1,this._verticallyScrolling=!1)}},{key:"_handleCloseDrag",value:function(t){if(this.isOpen){if(!this.options.draggable||this._isCurrentlyFixed()||this._verticallyScrolling)return;this.isDragged||this._startDrag(t),this._dragMoveUpdate(t);var e=this._xPos-this._startingXpos,i=0<e?"right":"left";e=Math.min(this._width,Math.abs(e)),this.options.edge!==i&&(e=0);var n=-e;"right"===this.options.edge&&(n=-n),this.percentOpen=Math.min(1,1-e/this._width),this.el.style.transform="translateX("+n+"px)",this._overlay.style.opacity=this.percentOpen}}},{key:"_handleCloseRelease",value:function(){this.isOpen&&this.isDragged&&(.8<this.percentOpen?this._animateIn():this.close(),this.isDragged=!1,this._verticallyScrolling=!1)}},{key:"_handleCloseTriggerClick",value:function(t){s(t.target).closest(".sidenav-close").length&&!this._isCurrentlyFixed()&&this.close()}},{key:"_handleWindowResize",value:function(){this.lastWindowWidth!==window.innerWidth&&(992<window.innerWidth?this.open():this.close()),this.lastWindowWidth=window.innerWidth,this.lastWindowHeight=window.innerHeight}},{key:"_setupClasses",value:function(){"right"===this.options.edge&&(this.el.classList.add("right-aligned"),this.dragTarget.classList.add("right-aligned"))}},{key:"_removeClasses",value:function(){this.el.classList.remove("right-aligned"),this.dragTarget.classList.remove("right-aligned")}},{key:"_setupFixed",value:function(){this._isCurrentlyFixed()&&this.open()}},{key:"_isCurrentlyFixed",value:function(){return this.isFixed&&992<window.innerWidth}},{key:"_createDragTarget",value:function(){var t=document.createElement("div");t.classList.add("drag-target"),document.body.appendChild(t),this.dragTarget=t}},{key:"_preventBodyScrolling",value:function(){document.body.style.overflow="hidden"}},{key:"_enableBodyScrolling",value:function(){document.body.style.overflow=""}},{key:"open",value:function(){!0!==this.isOpen&&(this.isOpen=!0,"function"==typeof this.options.onOpenStart&&this.options.onOpenStart.call(this,this.el),this._isCurrentlyFixed()?(o.remove(this.el),o({targets:this.el,translateX:0,duration:0,easing:"easeOutQuad"}),this._enableBodyScrolling(),this._overlay.style.display="none"):(this.options.preventScrolling&&this._preventBodyScrolling(),this.isDragged&&1==this.percentOpen||this._animateIn()))}},{key:"close",value:function(){if(!1!==this.isOpen)if(this.isOpen=!1,"function"==typeof this.options.onCloseStart&&this.options.onCloseStart.call(this,this.el),this._isCurrentlyFixed()){var t="left"===this.options.edge?"-105%":"105%";this.el.style.transform="translateX("+t+")"}else this._enableBodyScrolling(),this.isDragged&&0==this.percentOpen?this._overlay.style.display="none":this._animateOut()}},{key:"_animateIn",value:function(){this._animateSidenavIn(),this._animateOverlayIn()}},{key:"_animateSidenavIn",value:function(){var t=this,e="left"===this.options.edge?-1:1;this.isDragged&&(e="left"===this.options.edge?e+this.percentOpen:e-this.percentOpen),o.remove(this.el),o({targets:this.el,translateX:[100*e+"%",0],duration:this.options.inDuration,easing:"easeOutQuad",complete:function(){"function"==typeof t.options.onOpenEnd&&t.options.onOpenEnd.call(t,t.el)}})}},{key:"_animateOverlayIn",value:function(){var t=0;this.isDragged?t=this.percentOpen:s(this._overlay).css({display:"block"}),o.remove(this._overlay),o({targets:this._overlay,opacity:[t,1],duration:this.options.inDuration,easing:"easeOutQuad"})}},{key:"_animateOut",value:function(){this._animateSidenavOut(),this._animateOverlayOut()}},{key:"_animateSidenavOut",value:function(){var t=this,e="left"===this.options.edge?-1:1,i=0;this.isDragged&&(i="left"===this.options.edge?e+this.percentOpen:e-this.percentOpen),o.remove(this.el),o({targets:this.el,translateX:[100*i+"%",105*e+"%"],duration:this.options.outDuration,easing:"easeOutQuad",complete:function(){"function"==typeof t.options.onCloseEnd&&t.options.onCloseEnd.call(t,t.el)}})}},{key:"_animateOverlayOut",value:function(){var t=this;o.remove(this._overlay),o({targets:this._overlay,opacity:0,duration:this.options.outDuration,easing:"easeOutQuad",complete:function(){s(t._overlay).css("display","none")}})}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Sidenav}},{key:"defaults",get:function(){return e}}]),n}();t._sidenavs=[],M.Sidenav=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"sidenav","M_Sidenav")}(cash,M.anime),function(o,a){"use strict";var e={throttle:100,scrollOffset:200,activeClass:"active",getActiveElement:function(t){return'a[href="#'+t+'"]'}},t=function(t){function c(t,e){_classCallCheck(this,c);var i=_possibleConstructorReturn(this,(c.__proto__||Object.getPrototypeOf(c)).call(this,c,t,e));return(i.el.M_ScrollSpy=i).options=o.extend({},c.defaults,e),c._elements.push(i),c._count++,c._increment++,i.tickId=-1,i.id=c._increment,i._setupEventHandlers(),i._handleWindowScroll(),i}return _inherits(c,Component),_createClass(c,[{key:"destroy",value:function(){c._elements.splice(c._elements.indexOf(this),1),c._elementsInView.splice(c._elementsInView.indexOf(this),1),c._visibleElements.splice(c._visibleElements.indexOf(this.$el),1),c._count--,this._removeEventHandlers(),o(this.options.getActiveElement(this.$el.attr("id"))).removeClass(this.options.activeClass),this.el.M_ScrollSpy=void 0}},{key:"_setupEventHandlers",value:function(){var t=M.throttle(this._handleWindowScroll,200);this._handleThrottledResizeBound=t.bind(this),this._handleWindowScrollBound=this._handleWindowScroll.bind(this),1===c._count&&(window.addEventListener("scroll",this._handleWindowScrollBound),window.addEventListener("resize",this._handleThrottledResizeBound),document.body.addEventListener("click",this._handleTriggerClick))}},{key:"_removeEventHandlers",value:function(){0===c._count&&(window.removeEventListener("scroll",this._handleWindowScrollBound),window.removeEventListener("resize",this._handleThrottledResizeBound),document.body.removeEventListener("click",this._handleTriggerClick))}},{key:"_handleTriggerClick",value:function(t){for(var e=o(t.target),i=c._elements.length-1;0<=i;i--){var n=c._elements[i];if(e.is('a[href="javascript:void(0)'+n.$el.attr("id")+'"]')){t.preventDefault();var s=n.$el.offset().top+1;a({targets:[document.documentElement,document.body],scrollTop:s-n.options.scrollOffset,duration:400,easing:"easeOutCubic"});break}}}},{key:"_handleWindowScroll",value:function(){c._ticks++;for(var t=M.getDocumentScrollTop(),e=M.getDocumentScrollLeft(),i=e+window.innerWidth,n=t+window.innerHeight,s=c._findElements(t,i,n,e),o=0;o<s.length;o++){var a=s[o];a.tickId<0&&a._enter(),a.tickId=c._ticks}for(var r=0;r<c._elementsInView.length;r++){var l=c._elementsInView[r],h=l.tickId;0<=h&&h!==c._ticks&&(l._exit(),l.tickId=-1)}c._elementsInView=s}},{key:"_enter",value:function(){(c._visibleElements=c._visibleElements.filter(function(t){return 0!=t.height()}))[0]?(o(this.options.getActiveElement(c._visibleElements[0].attr("id"))).removeClass(this.options.activeClass),c._visibleElements[0][0].M_ScrollSpy&&this.id<c._visibleElements[0][0].M_ScrollSpy.id?c._visibleElements.unshift(this.$el):c._visibleElements.push(this.$el)):c._visibleElements.push(this.$el),o(this.options.getActiveElement(c._visibleElements[0].attr("id"))).addClass(this.options.activeClass)}},{key:"_exit",value:function(){var e=this;(c._visibleElements=c._visibleElements.filter(function(t){return 0!=t.height()}))[0]&&(o(this.options.getActiveElement(c._visibleElements[0].attr("id"))).removeClass(this.options.activeClass),(c._visibleElements=c._visibleElements.filter(function(t){return t.attr("id")!=e.$el.attr("id")}))[0]&&o(this.options.getActiveElement(c._visibleElements[0].attr("id"))).addClass(this.options.activeClass))}}],[{key:"init",value:function(t,e){return _get(c.__proto__||Object.getPrototypeOf(c),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_ScrollSpy}},{key:"_findElements",value:function(t,e,i,n){for(var s=[],o=0;o<c._elements.length;o++){var a=c._elements[o],r=t+a.options.scrollOffset||200;if(0<a.$el.height()){var l=a.$el.offset().top,h=a.$el.offset().left,d=h+a.$el.width(),u=l+a.$el.height();!(e<h||d<n||i<l||u<r)&&s.push(a)}}return s}},{key:"defaults",get:function(){return e}}]),c}();t._elements=[],t._elementsInView=[],t._visibleElements=[],t._count=0,t._increment=0,t._ticks=0,M.ScrollSpy=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"scrollSpy","M_ScrollSpy")}(cash,M.anime),function(h){"use strict";var e={data:{},limit:1/0,onAutocomplete:null,minLength:1,sortFunction:function(t,e,i){return t.indexOf(i)-e.indexOf(i)}},t=function(t){function s(t,e){_classCallCheck(this,s);var i=_possibleConstructorReturn(this,(s.__proto__||Object.getPrototypeOf(s)).call(this,s,t,e));return(i.el.M_Autocomplete=i).options=h.extend({},s.defaults,e),i.isOpen=!1,i.count=0,i.activeIndex=-1,i.oldVal,i.$inputField=i.$el.closest(".input-field"),i.$active=h(),i._mousedown=!1,i._setupMyDropdown(),i._setupEventHandlers(),i}return _inherits(s,Component),_createClass(s,[{key:"destroy",value:function(){this._removeEventHandlers(),this._removeMyDropdown(),this.el.M_Autocomplete=void 0}},{key:"_setupEventHandlers",value:function(){this._handleInputBlurBound=this._handleInputBlur.bind(this),this._handleInputKeyupAndFocusBound=this._handleInputKeyupAndFocus.bind(this),this._handleInputKeydownBound=this._handleInputKeydown.bind(this),this._handleInputClickBound=this._handleInputClick.bind(this),this._handleContainerMousedownAndTouchstartBound=this._handleContainerMousedownAndTouchstart.bind(this),this._handleContainerMouseupAndTouchendBound=this._handleContainerMouseupAndTouchend.bind(this),this.el.addEventListener("blur",this._handleInputBlurBound),this.el.addEventListener("keyup",this._handleInputKeyupAndFocusBound),this.el.addEventListener("focus",this._handleInputKeyupAndFocusBound),this.el.addEventListener("keydown",this._handleInputKeydownBound),this.el.addEventListener("click",this._handleInputClickBound),this.container.addEventListener("mousedown",this._handleContainerMousedownAndTouchstartBound),this.container.addEventListener("mouseup",this._handleContainerMouseupAndTouchendBound),void 0!==window.ontouchstart&&(this.container.addEventListener("touchstart",this._handleContainerMousedownAndTouchstartBound),this.container.addEventListener("touchend",this._handleContainerMouseupAndTouchendBound))}},{key:"_removeEventHandlers",value:function(){this.el.removeEventListener("blur",this._handleInputBlurBound),this.el.removeEventListener("keyup",this._handleInputKeyupAndFocusBound),this.el.removeEventListener("focus",this._handleInputKeyupAndFocusBound),this.el.removeEventListener("keydown",this._handleInputKeydownBound),this.el.removeEventListener("click",this._handleInputClickBound),this.container.removeEventListener("mousedown",this._handleContainerMousedownAndTouchstartBound),this.container.removeEventListener("mouseup",this._handleContainerMouseupAndTouchendBound),void 0!==window.ontouchstart&&(this.container.removeEventListener("touchstart",this._handleContainerMousedownAndTouchstartBound),this.container.removeEventListener("touchend",this._handleContainerMouseupAndTouchendBound))}},{key:"_setupMyDropdown",value:function(){var e=this;this.container=document.createElement("ul"),this.container.id="autocomplete-options-"+M.guid(),h(this.container).addClass("autocomplete-content dropdown-content"),this.$inputField.append(this.container),this.el.setAttribute("mydata-target",this.container.id),this.dropdown=M.MyDropdown.init(this.el,{autoFocus:!1,closeOnClick:!1,coverTrigger:!1,onItemClick:function(t){e.selectOption(h(t))}}),this.el.removeEventListener("click",this.dropdown._handleClickBound)}},{key:"_removeMyDropdown",value:function(){this.container.parentNode.removeChild(this.container)}},{key:"_handleInputBlur",value:function(){this._mousedown||(this.close(),this._resetAutocomplete())}},{key:"_handleInputKeyupAndFocus",value:function(t){"keyup"===t.type&&(s._keydown=!1),this.count=0;var e=this.el.value.toLowerCase();13!==t.keyCode&&38!==t.keyCode&&40!==t.keyCode&&(this.oldVal===e||!M.tabPressed&&"focus"===t.type||this.open(),this.oldVal=e)}},{key:"_handleInputKeydown",value:function(t){s._keydown=!0;var e=t.keyCode,i=void 0,n=h(this.container).children("li").length;e===M.keys.ENTER&&0<=this.activeIndex?(i=h(this.container).children("li").eq(this.activeIndex)).length&&(this.selectOption(i),t.preventDefault()):e!==M.keys.ARROW_UP&&e!==M.keys.ARROW_DOWN||(t.preventDefault(),e===M.keys.ARROW_UP&&0<this.activeIndex&&this.activeIndex--,e===M.keys.ARROW_DOWN&&this.activeIndex<n-1&&this.activeIndex++,this.$active.removeClass("active"),0<=this.activeIndex&&(this.$active=h(this.container).children("li").eq(this.activeIndex),this.$active.addClass("active")))}},{key:"_handleInputClick",value:function(t){this.open()}},{key:"_handleContainerMousedownAndTouchstart",value:function(t){this._mousedown=!0}},{key:"_handleContainerMouseupAndTouchend",value:function(t){this._mousedown=!1}},{key:"_highlight",value:function(t,e){var i=e.find("img"),n=e.text().toLowerCase().indexOf(""+t.toLowerCase()),s=n+t.length-1,o=e.text().slice(0,n),a=e.text().slice(n,s+1),r=e.text().slice(s+1);e.html("<span>"+o+"<span class='highlight'>"+a+"</span>"+r+"</span>"),i.length&&e.prepend(i)}},{key:"_resetCurrentElement",value:function(){this.activeIndex=-1,this.$active.removeClass("active")}},{key:"_resetAutocomplete",value:function(){h(this.container).empty(),this._resetCurrentElement(),this.oldVal=null,this.isOpen=!1,this._mousedown=!1}},{key:"selectOption",value:function(t){var e=t.text().trim();this.el.value=e,this.$el.trigger("change"),this._resetAutocomplete(),this.close(),"function"==typeof this.options.onAutocomplete&&this.options.onAutocomplete.call(this,e)}},{key:"_renderMyDropdown",value:function(t,i){var n=this;this._resetAutocomplete();var e=[];for(var s in t)if(t.hasOwnProperty(s)&&-1!==s.toLowerCase().indexOf(i)){if(this.count>=this.options.limit)break;var o={data:t[s],key:s};e.push(o),this.count++}if(this.options.sortFunction){e.sort(function(t,e){return n.options.sortFunction(t.key.toLowerCase(),e.key.toLowerCase(),i.toLowerCase())})}for(var a=0;a<e.length;a++){var r=e[a],l=h("<li></li>");r.data?l.append('<img src="'+r.data+'" class="right circle"><span>'+r.key+"</span>"):l.append("<span>"+r.key+"</span>"),h(this.container).append(l),this._highlight(i,l)}}},{key:"open",value:function(){var t=this.el.value.toLowerCase();this._resetAutocomplete(),t.length>=this.options.minLength&&(this.isOpen=!0,this._renderMyDropdown(this.options.data,t)),this.dropdown.isOpen?this.dropdown.recalculateDimensions():this.dropdown.open()}},{key:"close",value:function(){this.dropdown.close()}},{key:"updateData",value:function(t){var e=this.el.value.toLowerCase();this.options.data=t,this.isOpen&&this._renderMyDropdown(t,e)}}],[{key:"init",value:function(t,e){return _get(s.__proto__||Object.getPrototypeOf(s),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Autocomplete}},{key:"defaults",get:function(){return e}}]),s}();t._keydown=!1,M.Autocomplete=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"autocomplete","M_Autocomplete")}(cash),function(d){M.updateTextFields=function(){d("input[type=text], input[type=password], input[type=email], input[type=url], input[type=tel], input[type=number], input[type=search], input[type=date], input[type=time], textarea").each(function(t,e){var i=d(this);0<t.value.length||d(t).is(":focus")||t.autofocus||null!==i.attr("placeholder")?i.siblings("label").addClass("active"):t.validity?i.siblings("label").toggleClass("active",!0===t.validity.badInput):i.siblings("label").removeClass("active")})},M.validate_field=function(t){var e=null!==t.attr("data-length"),i=parseInt(t.attr("data-length")),n=t[0].value.length;0!==n||!1!==t[0].validity.badInput||t.is(":required")?t.hasClass("validate")&&(t.is(":valid")&&e&&n<=i||t.is(":valid")&&!e?(t.removeClass("invalid"),t.addClass("valid")):(t.removeClass("valid"),t.addClass("invalid"))):t.hasClass("validate")&&(t.removeClass("valid"),t.removeClass("invalid"))},M.textareaAutoResize=function(t){if(t instanceof Element&&(t=d(t)),t.length){var e=d(".hiddendiv").first();e.length||(e=d('<div class="hiddendiv common"></div>'),d("body").append(e));var i=t.css("font-family"),n=t.css("font-size"),s=t.css("line-height"),o=t.css("padding-top"),a=t.css("padding-right"),r=t.css("padding-bottom"),l=t.css("padding-left");n&&e.css("font-size",n),i&&e.css("font-family",i),s&&e.css("line-height",s),o&&e.css("padding-top",o),a&&e.css("padding-right",a),r&&e.css("padding-bottom",r),l&&e.css("padding-left",l),t.data("original-height")||t.data("original-height",t.height()),"off"===t.attr("wrap")&&e.css("overflow-wrap","normal").css("white-space","pre"),e.text(t[0].value+"\n");var h=e.html().replace(/\n/g,"<br>");e.html(h),0<t[0].offsetWidth&&0<t[0].offsetHeight?e.css("width",t.width()+"px"):e.css("width",window.innerWidth/2+"px"),t.data("original-height")<=e.innerHeight()?t.css("height",e.innerHeight()+"px"):t[0].value.length<t.data("previous-length")&&t.css("height",t.data("original-height")+"px"),t.data("previous-length",t[0].value.length)}else console.error("No textarea element found")},d(document).ready(function(){var n="input[type=text], input[type=password], input[type=email], input[type=url], input[type=tel], input[type=number], input[type=search], input[type=date], input[type=time], textarea";d(document).on("change",n,function(){0===this.value.length&&null===d(this).attr("placeholder")||d(this).siblings("label").addClass("active"),M.validate_field(d(this))}),d(document).ready(function(){M.updateTextFields()}),d(document).on("reset",function(t){var e=d(t.target);e.is("form")&&(e.find(n).removeClass("valid").removeClass("invalid"),e.find(n).each(function(t){this.value.length&&d(this).siblings("label").removeClass("active")}),setTimeout(function(){e.find("select").each(function(){this.M_FormSelect&&d(this).trigger("change")})},0))}),document.addEventListener("focus",function(t){d(t.target).is(n)&&d(t.target).siblings("label, .prefix").addClass("active")},!0),document.addEventListener("blur",function(t){var e=d(t.target);if(e.is(n)){var i=".prefix";0===e[0].value.length&&!0!==e[0].validity.badInput&&null===e.attr("placeholder")&&(i+=", label"),e.siblings(i).removeClass("active"),M.validate_field(e)}},!0);d(document).on("keyup","input[type=radio], input[type=checkbox]",function(t){if(t.which===M.keys.TAB)return d(this).addClass("tabbed"),void d(this).one("blur",function(t){d(this).removeClass("tabbed")})});var t=".materialize-textarea";d(t).each(function(){var t=d(this);t.data("original-height",t.height()),t.data("previous-length",this.value.length),M.textareaAutoResize(t)}),d(document).on("keyup",t,function(){M.textareaAutoResize(d(this))}),d(document).on("keydown",t,function(){M.textareaAutoResize(d(this))}),d(document).on("change",'.file-field input[type="file"]',function(){for(var t=d(this).closest(".file-field").find("input.file-path"),e=d(this)[0].files,i=[],n=0;n<e.length;n++)i.push(e[n].name);t[0].value=i.join(", "),t.trigger("change")})})}(cash),function(s,o){"use strict";var e={indicators:!0,height:400,duration:500,interval:6e3},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return(i.el.M_Slider=i).options=s.extend({},n.defaults,e),i.$slider=i.$el.find(".slides"),i.$slides=i.$slider.children("li"),i.activeIndex=i.$slides.filter(function(t){return s(t).hasClass("active")}).first().index(),-1!=i.activeIndex&&(i.$active=i.$slides.eq(i.activeIndex)),i._setSliderHeight(),i.$slides.find(".caption").each(function(t){i._animateCaptionIn(t,0)}),i.$slides.find("img").each(function(t){var e="data:image/gif;base64,R0lGODlhAQABAIABAP///wAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==";s(t).attr("src")!==e&&(s(t).css("background-image",'url("'+s(t).attr("src")+'")'),s(t).attr("src",e))}),i._setupIndicators(),i.$active?i.$active.css("display","block"):(i.$slides.first().addClass("active"),o({targets:i.$slides.first()[0],opacity:1,duration:i.options.duration,easing:"easeOutQuad"}),i.activeIndex=0,i.$active=i.$slides.eq(i.activeIndex),i.options.indicators&&i.$indicators.eq(i.activeIndex).addClass("active")),i.$active.find("img").each(function(t){o({targets:i.$active.find(".caption")[0],opacity:1,translateX:0,translateY:0,duration:i.options.duration,easing:"easeOutQuad"})}),i._setupEventHandlers(),i.start(),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){this.pause(),this._removeIndicators(),this._removeEventHandlers(),this.el.M_Slider=void 0}},{key:"_setupEventHandlers",value:function(){var e=this;this._handleIntervalBound=this._handleInterval.bind(this),this._handleIndicatorClickBound=this._handleIndicatorClick.bind(this),this.options.indicators&&this.$indicators.each(function(t){t.addEventListener("click",e._handleIndicatorClickBound)})}},{key:"_removeEventHandlers",value:function(){var e=this;this.options.indicators&&this.$indicators.each(function(t){t.removeEventListener("click",e._handleIndicatorClickBound)})}},{key:"_handleIndicatorClick",value:function(t){var e=s(t.target).index();this.set(e)}},{key:"_handleInterval",value:function(){var t=this.$slider.find(".active").index();this.$slides.length===t+1?t=0:t+=1,this.set(t)}},{key:"_animateCaptionIn",value:function(t,e){var i={targets:t,opacity:0,duration:e,easing:"easeOutQuad"};s(t).hasClass("center-align")?i.translateY=-100:s(t).hasClass("right-align")?i.translateX=100:s(t).hasClass("left-align")&&(i.translateX=-100),o(i)}},{key:"_setSliderHeight",value:function(){this.$el.hasClass("fullscreen")||(this.options.indicators?this.$el.css("height",this.options.height+40+"px"):this.$el.css("height",this.options.height+"px"),this.$slider.css("height",this.options.height+"px"))}},{key:"_setupIndicators",value:function(){var n=this;this.options.indicators&&(this.$indicators=s('<ul class="indicators"></ul>'),this.$slides.each(function(t,e){var i=s('<li class="indicator-item"></li>');n.$indicators.append(i[0])}),this.$el.append(this.$indicators[0]),this.$indicators=this.$indicators.children("li.indicator-item"))}},{key:"_removeIndicators",value:function(){this.$el.find("ul.indicators").remove()}},{key:"set",value:function(t){var e=this;if(t>=this.$slides.length?t=0:t<0&&(t=this.$slides.length-1),this.activeIndex!=t){this.$active=this.$slides.eq(this.activeIndex);var i=this.$active.find(".caption");this.$active.removeClass("active"),o({targets:this.$active[0],opacity:0,duration:this.options.duration,easing:"easeOutQuad",complete:function(){e.$slides.not(".active").each(function(t){o({targets:t,opacity:0,translateX:0,translateY:0,duration:0,easing:"easeOutQuad"})})}}),this._animateCaptionIn(i[0],this.options.duration),this.options.indicators&&(this.$indicators.eq(this.activeIndex).removeClass("active"),this.$indicators.eq(t).addClass("active")),o({targets:this.$slides.eq(t)[0],opacity:1,duration:this.options.duration,easing:"easeOutQuad"}),o({targets:this.$slides.eq(t).find(".caption")[0],opacity:1,translateX:0,translateY:0,duration:this.options.duration,delay:this.options.duration,easing:"easeOutQuad"}),this.$slides.eq(t).addClass("active"),this.activeIndex=t,this.start()}}},{key:"pause",value:function(){clearInterval(this.interval)}},{key:"start",value:function(){clearInterval(this.interval),this.interval=setInterval(this._handleIntervalBound,this.options.duration+this.options.interval)}},{key:"next",value:function(){var t=this.activeIndex+1;t>=this.$slides.length?t=0:t<0&&(t=this.$slides.length-1),this.set(t)}},{key:"prev",value:function(){var t=this.activeIndex-1;t>=this.$slides.length?t=0:t<0&&(t=this.$slides.length-1),this.set(t)}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Slider}},{key:"defaults",get:function(){return e}}]),n}();M.Slider=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"slider","M_Slider")}(cash,M.anime),function(n,s){n(document).on("click",".card",function(t){if(n(this).children(".card-reveal").length){var i=n(t.target).closest(".card");void 0===i.data("initialOverflow")&&i.data("initialOverflow",void 0===i.css("overflow")?"":i.css("overflow"));var e=n(this).find(".card-reveal");n(t.target).is(n(".card-reveal .card-title"))||n(t.target).is(n(".card-reveal .card-title i"))?s({targets:e[0],translateY:0,duration:225,easing:"easeInOutQuad",complete:function(t){var e=t.animatables[0].target;n(e).css({display:"none"}),i.css("overflow",i.data("initialOverflow"))}}):(n(t.target).is(n(".card .activator"))||n(t.target).is(n(".card .activator i")))&&(i.css("overflow","hidden"),e.css({display:"block"}),s({targets:e[0],translateY:"-100%",duration:300,easing:"easeInOutQuad"}))}})}(cash,M.anime),function(h){"use strict";var e={data:[],placeholder:"",secondaryPlaceholder:"",autocompleteOptions:{},limit:1/0,onChipAdd:null,onChipSelect:null,onChipDelete:null},t=function(t){function l(t,e){_classCallCheck(this,l);var i=_possibleConstructorReturn(this,(l.__proto__||Object.getPrototypeOf(l)).call(this,l,t,e));return(i.el.M_Chips=i).options=h.extend({},l.defaults,e),i.$el.addClass("chips input-field"),i.chipsData=[],i.$chips=h(),i._setupInput(),i.hasAutocomplete=0<Object.keys(i.options.autocompleteOptions).length,i.$input.attr("id")||i.$input.attr("id",M.guid()),i.options.data.length&&(i.chipsData=i.options.data,i._renderChips(i.chipsData)),i.hasAutocomplete&&i._setupAutocomplete(),i._setPlaceholder(),i._setupLabel(),i._setupEventHandlers(),i}return _inherits(l,Component),_createClass(l,[{key:"getData",value:function(){return this.chipsData}},{key:"destroy",value:function(){this._removeEventHandlers(),this.$chips.remove(),this.el.M_Chips=void 0}},{key:"_setupEventHandlers",value:function(){this._handleChipClickBound=this._handleChipClick.bind(this),this._handleInputKeydownBound=this._handleInputKeydown.bind(this),this._handleInputFocusBound=this._handleInputFocus.bind(this),this._handleInputBlurBound=this._handleInputBlur.bind(this),this.el.addEventListener("click",this._handleChipClickBound),document.addEventListener("keydown",l._handleChipsKeydown),document.addEventListener("keyup",l._handleChipsKeyup),this.el.addEventListener("blur",l._handleChipsBlur,!0),this.$input[0].addEventListener("focus",this._handleInputFocusBound),this.$input[0].addEventListener("blur",this._handleInputBlurBound),this.$input[0].addEventListener("keydown",this._handleInputKeydownBound)}},{key:"_removeEventHandlers",value:function(){this.el.removeEventListener("click",this._handleChipClickBound),document.removeEventListener("keydown",l._handleChipsKeydown),document.removeEventListener("keyup",l._handleChipsKeyup),this.el.removeEventListener("blur",l._handleChipsBlur,!0),this.$input[0].removeEventListener("focus",this._handleInputFocusBound),this.$input[0].removeEventListener("blur",this._handleInputBlurBound),this.$input[0].removeEventListener("keydown",this._handleInputKeydownBound)}},{key:"_handleChipClick",value:function(t){var e=h(t.target).closest(".chip"),i=h(t.target).is(".close");if(e.length){var n=e.index();i?(this.deleteChip(n),this.$input[0].focus()):this.selectChip(n)}else this.$input[0].focus()}},{key:"_handleInputFocus",value:function(){this.$el.addClass("focus")}},{key:"_handleInputBlur",value:function(){this.$el.removeClass("focus")}},{key:"_handleInputKeydown",value:function(t){if(l._keydown=!0,13===t.keyCode){if(this.hasAutocomplete&&this.autocomplete&&this.autocomplete.isOpen)return;t.preventDefault(),this.addChip({tag:this.$input[0].value}),this.$input[0].value=""}else 8!==t.keyCode&&37!==t.keyCode||""!==this.$input[0].value||!this.chipsData.length||(t.preventDefault(),this.selectChip(this.chipsData.length-1))}},{key:"_renderChip",value:function(t){if(t.tag){var e=document.createElement("div"),i=document.createElement("i");if(e.classList.add("chip"),e.textContent=t.tag,e.setAttribute("tabindex",0),h(i).addClass("material-icons close"),i.textContent="close",t.image){var n=document.createElement("img");n.setAttribute("src",t.image),e.insertBefore(n,e.firstChild)}return e.appendChild(i),e}}},{key:"_renderChips",value:function(){this.$chips.remove();for(var t=0;t<this.chipsData.length;t++){var e=this._renderChip(this.chipsData[t]);this.$el.append(e),this.$chips.add(e)}this.$el.append(this.$input[0])}},{key:"_setupAutocomplete",value:function(){var e=this;this.options.autocompleteOptions.onAutocomplete=function(t){e.addChip({tag:t}),e.$input[0].value="",e.$input[0].focus()},this.autocomplete=M.Autocomplete.init(this.$input[0],this.options.autocompleteOptions)}},{key:"_setupInput",value:function(){this.$input=this.$el.find("input"),this.$input.length||(this.$input=h("<input></input>"),this.$el.append(this.$input)),this.$input.addClass("input")}},{key:"_setupLabel",value:function(){this.$label=this.$el.find("label"),this.$label.length&&this.$label.setAttribute("for",this.$input.attr("id"))}},{key:"_setPlaceholder",value:function(){void 0!==this.chipsData&&!this.chipsData.length&&this.options.placeholder?h(this.$input).prop("placeholder",this.options.placeholder):(void 0===this.chipsData||this.chipsData.length)&&this.options.secondaryPlaceholder&&h(this.$input).prop("placeholder",this.options.secondaryPlaceholder)}},{key:"_isValid",value:function(t){if(t.hasOwnProperty("tag")&&""!==t.tag){for(var e=!1,i=0;i<this.chipsData.length;i++)if(this.chipsData[i].tag===t.tag){e=!0;break}return!e}return!1}},{key:"addChip",value:function(t){if(this._isValid(t)&&!(this.chipsData.length>=this.options.limit)){var e=this._renderChip(t);this.$chips.add(e),this.chipsData.push(t),h(this.$input).before(e),this._setPlaceholder(),"function"==typeof this.options.onChipAdd&&this.options.onChipAdd.call(this,this.$el,e)}}},{key:"deleteChip",value:function(t){var e=this.$chips.eq(t);this.$chips.eq(t).remove(),this.$chips=this.$chips.filter(function(t){return 0<=h(t).index()}),this.chipsData.splice(t,1),this._setPlaceholder(),"function"==typeof this.options.onChipDelete&&this.options.onChipDelete.call(this,this.$el,e[0])}},{key:"selectChip",value:function(t){var e=this.$chips.eq(t);(this._selectedChip=e)[0].focus(),"function"==typeof this.options.onChipSelect&&this.options.onChipSelect.call(this,this.$el,e[0])}}],[{key:"init",value:function(t,e){return _get(l.__proto__||Object.getPrototypeOf(l),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Chips}},{key:"_handleChipsKeydown",value:function(t){l._keydown=!0;var e=h(t.target).closest(".chips"),i=t.target&&e.length;if(!h(t.target).is("input, textarea")&&i){var n=e[0].M_Chips;if(8===t.keyCode||46===t.keyCode){t.preventDefault();var s=n.chipsData.length;if(n._selectedChip){var o=n._selectedChip.index();n.deleteChip(o),n._selectedChip=null,s=Math.max(o-1,0)}n.chipsData.length&&n.selectChip(s)}else if(37===t.keyCode){if(n._selectedChip){var a=n._selectedChip.index()-1;if(a<0)return;n.selectChip(a)}}else if(39===t.keyCode&&n._selectedChip){var r=n._selectedChip.index()+1;r>=n.chipsData.length?n.$input[0].focus():n.selectChip(r)}}}},{key:"_handleChipsKeyup",value:function(t){l._keydown=!1}},{key:"_handleChipsBlur",value:function(t){l._keydown||(h(t.target).closest(".chips")[0].M_Chips._selectedChip=null)}},{key:"defaults",get:function(){return e}}]),l}();t._keydown=!1,M.Chips=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"chips","M_Chips"),h(document).ready(function(){h(document.body).on("click",".chip .close",function(){var t=h(this).closest(".chips");t.length&&t[0].M_Chips||h(this).closest(".chip").remove()})})}(cash),function(s){"use strict";var e={top:0,bottom:1/0,offset:0,onPositionChange:null},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return(i.el.M_Pushpin=i).options=s.extend({},n.defaults,e),i.originalOffset=i.el.offsetTop,n._pushpins.push(i),i._setupEventHandlers(),i._updatePosition(),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){this.el.style.top=null,this._removePinClasses(),this._removeEventHandlers();var t=n._pushpins.indexOf(this);n._pushpins.splice(t,1)}},{key:"_setupEventHandlers",value:function(){document.addEventListener("scroll",n._updateElements)}},{key:"_removeEventHandlers",value:function(){document.removeEventListener("scroll",n._updateElements)}},{key:"_updatePosition",value:function(){var t=M.getDocumentScrollTop()+this.options.offset;this.options.top<=t&&this.options.bottom>=t&&!this.el.classList.contains("pinned")&&(this._removePinClasses(),this.el.style.top=this.options.offset+"px",this.el.classList.add("pinned"),"function"==typeof this.options.onPositionChange&&this.options.onPositionChange.call(this,"pinned")),t<this.options.top&&!this.el.classList.contains("pin-top")&&(this._removePinClasses(),this.el.style.top=0,this.el.classList.add("pin-top"),"function"==typeof this.options.onPositionChange&&this.options.onPositionChange.call(this,"pin-top")),t>this.options.bottom&&!this.el.classList.contains("pin-bottom")&&(this._removePinClasses(),this.el.classList.add("pin-bottom"),this.el.style.top=this.options.bottom-this.originalOffset+"px","function"==typeof this.options.onPositionChange&&this.options.onPositionChange.call(this,"pin-bottom"))}},{key:"_removePinClasses",value:function(){this.el.classList.remove("pin-top"),this.el.classList.remove("pinned"),this.el.classList.remove("pin-bottom")}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Pushpin}},{key:"_updateElements",value:function(){for(var t in n._pushpins){n._pushpins[t]._updatePosition()}}},{key:"defaults",get:function(){return e}}]),n}();t._pushpins=[],M.Pushpin=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"pushpin","M_Pushpin")}(cash),function(r,s){"use strict";var e={direction:"top",hoverEnabled:!0,toolbarEnabled:!1};r.fn.reverse=[].reverse;var t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return(i.el.M_FloatingActionButton=i).options=r.extend({},n.defaults,e),i.isOpen=!1,i.$anchor=i.$el.children("a").first(),i.$menu=i.$el.children("ul").first(),i.$floatingBtns=i.$el.find("ul .btn-floating"),i.$floatingBtnsReverse=i.$el.find("ul .btn-floating").reverse(),i.offsetY=0,i.offsetX=0,i.$el.addClass("direction-"+i.options.direction),"top"===i.options.direction?i.offsetY=40:"right"===i.options.direction?i.offsetX=-40:"bottom"===i.options.direction?i.offsetY=-40:i.offsetX=40,i._setupEventHandlers(),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){this._removeEventHandlers(),this.el.M_FloatingActionButton=void 0}},{key:"_setupEventHandlers",value:function(){this._handleFABClickBound=this._handleFABClick.bind(this),this._handleOpenBound=this.open.bind(this),this._handleCloseBound=this.close.bind(this),this.options.hoverEnabled&&!this.options.toolbarEnabled?(this.el.addEventListener("mouseenter",this._handleOpenBound),this.el.addEventListener("mouseleave",this._handleCloseBound)):this.el.addEventListener("click",this._handleFABClickBound)}},{key:"_removeEventHandlers",value:function(){this.options.hoverEnabled&&!this.options.toolbarEnabled?(this.el.removeEventListener("mouseenter",this._handleOpenBound),this.el.removeEventListener("mouseleave",this._handleCloseBound)):this.el.removeEventListener("click",this._handleFABClickBound)}},{key:"_handleFABClick",value:function(){this.isOpen?this.close():this.open()}},{key:"_handleDocumentClick",value:function(t){r(t.target).closest(this.$menu).length||this.close()}},{key:"open",value:function(){this.isOpen||(this.options.toolbarEnabled?this._animateInToolbar():this._animateInFAB(),this.isOpen=!0)}},{key:"close",value:function(){this.isOpen&&(this.options.toolbarEnabled?(window.removeEventListener("scroll",this._handleCloseBound,!0),document.body.removeEventListener("click",this._handleDocumentClickBound,!0),this._animateOutToolbar()):this._animateOutFAB(),this.isOpen=!1)}},{key:"_animateInFAB",value:function(){var e=this;this.$el.addClass("active");var i=0;this.$floatingBtnsReverse.each(function(t){s({targets:t,opacity:1,scale:[.4,1],translateY:[e.offsetY,0],translateX:[e.offsetX,0],duration:275,delay:i,easing:"easeInOutQuad"}),i+=40})}},{key:"_animateOutFAB",value:function(){var e=this;this.$floatingBtnsReverse.each(function(t){s.remove(t),s({targets:t,opacity:0,scale:.4,translateY:e.offsetY,translateX:e.offsetX,duration:175,easing:"easeOutQuad",complete:function(){e.$el.removeClass("active")}})})}},{key:"_animateInToolbar",value:function(){var t,e=this,i=window.innerWidth,n=window.innerHeight,s=this.el.getBoundingClientRect(),o=r('<div class="fab-backdrop"></div>'),a=this.$anchor.css("background-color");this.$anchor.append(o),this.offsetX=s.left-i/2+s.width/2,this.offsetY=n-s.bottom,t=i/o[0].clientWidth,this.btnBottom=s.bottom,this.btnLeft=s.left,this.btnWidth=s.width,this.$el.addClass("active"),this.$el.css({"text-align":"center",width:"100%",bottom:0,left:0,transform:"translateX("+this.offsetX+"px)",transition:"none"}),this.$anchor.css({transform:"translateY("+-this.offsetY+"px)",transition:"none"}),o.css({"background-color":a}),setTimeout(function(){e.$el.css({transform:"",transition:"transform .2s cubic-bezier(0.550, 0.085, 0.680, 0.530), background-color 0s linear .2s"}),e.$anchor.css({overflow:"visible",transform:"",transition:"transform .2s"}),setTimeout(function(){e.$el.css({overflow:"hidden","background-color":a}),o.css({transform:"scale("+t+")",transition:"transform .2s cubic-bezier(0.550, 0.055, 0.675, 0.190)"}),e.$menu.children("li").children("a").css({opacity:1}),e._handleDocumentClickBound=e._handleDocumentClick.bind(e),window.addEventListener("scroll",e._handleCloseBound,!0),document.body.addEventListener("click",e._handleDocumentClickBound,!0)},100)},0)}},{key:"_animateOutToolbar",value:function(){var t=this,e=window.innerWidth,i=window.innerHeight,n=this.$el.find(".fab-backdrop"),s=this.$anchor.css("background-color");this.offsetX=this.btnLeft-e/2+this.btnWidth/2,this.offsetY=i-this.btnBottom,this.$el.removeClass("active"),this.$el.css({"background-color":"transparent",transition:"none"}),this.$anchor.css({transition:"none"}),n.css({transform:"scale(0)","background-color":s}),this.$menu.children("li").children("a").css({opacity:""}),setTimeout(function(){n.remove(),t.$el.css({"text-align":"",width:"",bottom:"",left:"",overflow:"","background-color":"",transform:"translate3d("+-t.offsetX+"px,0,0)"}),t.$anchor.css({overflow:"",transform:"translate3d(0,"+t.offsetY+"px,0)"}),setTimeout(function(){t.$el.css({transform:"translate3d(0,0,0)",transition:"transform .2s"}),t.$anchor.css({transform:"translate3d(0,0,0)",transition:"transform .2s cubic-bezier(0.550, 0.055, 0.675, 0.190)"})},20)},200)}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_FloatingActionButton}},{key:"defaults",get:function(){return e}}]),n}();M.FloatingActionButton=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"floatingActionButton","M_FloatingActionButton")}(cash,M.anime),function(g){"use strict";var e={autoClose:!1,format:"mmm dd, yyyy",parse:null,defaultDate:null,setDefaultDate:!1,disableWeekends:!1,disableDayFn:null,firstDay:0,minDate:null,maxDate:null,yearRange:10,minYear:0,maxYear:9999,minMonth:void 0,maxMonth:void 0,startRange:null,endRange:null,isRTL:!1,showMonthAfterYear:!1,showDaysInNextAndPreviousMonths:!1,container:null,showClearBtn:!1,i18n:{cancel:"Cancel",clear:"Clear",done:"Ok",previousMonth:"‹",nextMonth:"›",months:["January","February","March","April","May","June","July","August","September","October","November","December"],monthsShort:["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],weekdays:["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],weekdaysShort:["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],weekdaysAbbrev:["S","M","T","W","T","F","S"]},events:[],onSelect:null,onOpen:null,onClose:null,onDraw:null},t=function(t){function B(t,e){_classCallCheck(this,B);var i=_possibleConstructorReturn(this,(B.__proto__||Object.getPrototypeOf(B)).call(this,B,t,e));(i.el.M_Datepicker=i).options=g.extend({},B.defaults,e),e&&e.hasOwnProperty("i18n")&&"object"==typeof e.i18n&&(i.options.i18n=g.extend({},B.defaults.i18n,e.i18n)),i.options.minDate&&i.options.minDate.setHours(0,0,0,0),i.options.maxDate&&i.options.maxDate.setHours(0,0,0,0),i.id=M.guid(),i._setupVariables(),i._insertHTMLIntoDOM(),i._setupModal(),i._setupEventHandlers(),i.options.defaultDate||(i.options.defaultDate=new Date(Date.parse(i.el.value)));var n=i.options.defaultDate;return B._isDate(n)?i.options.setDefaultDate?(i.setDate(n,!0),i.setInputValue()):i.gotoDate(n):i.gotoDate(new Date),i.isOpen=!1,i}return _inherits(B,Component),_createClass(B,[{key:"destroy",value:function(){this._removeEventHandlers(),this.modal.destroy(),g(this.modalEl).remove(),this.destroySelects(),this.el.M_Datepicker=void 0}},{key:"destroySelects",value:function(){var t=this.calendarEl.querySelector(".orig-select-year");t&&M.FormSelect.getInstance(t).destroy();var e=this.calendarEl.querySelector(".orig-select-month");e&&M.FormSelect.getInstance(e).destroy()}},{key:"_insertHTMLIntoDOM",value:function(){this.options.showClearBtn&&(g(this.clearBtn).css({visibility:""}),this.clearBtn.innerHTML=this.options.i18n.clear),this.doneBtn.innerHTML=this.options.i18n.done,this.cancelBtn.innerHTML=this.options.i18n.cancel,this.options.container?this.$modalEl.appendTo(this.options.container):this.$modalEl.insertBefore(this.el)}},{key:"_setupModal",value:function(){var t=this;this.modalEl.id="modal-"+this.id,this.modal=M.Modal.init(this.modalEl,{onCloseEnd:function(){t.isOpen=!1}})}},{key:"toString",value:function(t){var e=this;return t=t||this.options.format,B._isDate(this.date)?t.split(/(d{1,4}|m{1,4}|y{4}|yy|!.)/g).map(function(t){return e.formats[t]?e.formats[t]():t}).join(""):""}},{key:"setDate",value:function(t,e){if(!t)return this.date=null,this._renderDateDisplay(),this.draw();if("string"==typeof t&&(t=new Date(Date.parse(t))),B._isDate(t)){var i=this.options.minDate,n=this.options.maxDate;B._isDate(i)&&t<i?t=i:B._isDate(n)&&n<t&&(t=n),this.date=new Date(t.getTime()),this._renderDateDisplay(),B._setToStartOfDay(this.date),this.gotoDate(this.date),e||"function"!=typeof this.options.onSelect||this.options.onSelect.call(this,this.date)}}},{key:"setInputValue",value:function(){this.el.value=this.toString(),this.$el.trigger("change",{firedBy:this})}},{key:"_renderDateDisplay",value:function(){var t=B._isDate(this.date)?this.date:new Date,e=this.options.i18n,i=e.weekdaysShort[t.getDay()],n=e.monthsShort[t.getMonth()],s=t.getDate();this.yearTextEl.innerHTML=t.getFullYear(),this.dateTextEl.innerHTML=i+", "+n+" "+s}},{key:"gotoDate",value:function(t){var e=!0;if(B._isDate(t)){if(this.calendars){var i=new Date(this.calendars[0].year,this.calendars[0].month,1),n=new Date(this.calendars[this.calendars.length-1].year,this.calendars[this.calendars.length-1].month,1),s=t.getTime();n.setMonth(n.getMonth()+1),n.setDate(n.getDate()-1),e=s<i.getTime()||n.getTime()<s}e&&(this.calendars=[{month:t.getMonth(),year:t.getFullYear()}]),this.adjustCalendars()}}},{key:"adjustCalendars",value:function(){this.calendars[0]=this.adjustCalendar(this.calendars[0]),this.draw()}},{key:"adjustCalendar",value:function(t){return t.month<0&&(t.year-=Math.ceil(Math.abs(t.month)/12),t.month+=12),11<t.month&&(t.year+=Math.floor(Math.abs(t.month)/12),t.month-=12),t}},{key:"nextMonth",value:function(){this.calendars[0].month++,this.adjustCalendars()}},{key:"prevMonth",value:function(){this.calendars[0].month--,this.adjustCalendars()}},{key:"render",value:function(t,e,i){var n=this.options,s=new Date,o=B._getDaysInMonth(t,e),a=new Date(t,e,1).getDay(),r=[],l=[];B._setToStartOfDay(s),0<n.firstDay&&(a-=n.firstDay)<0&&(a+=7);for(var h=0===e?11:e-1,d=11===e?0:e+1,u=0===e?t-1:t,c=11===e?t+1:t,p=B._getDaysInMonth(u,h),v=o+a,f=v;7<f;)f-=7;v+=7-f;for(var m=!1,g=0,_=0;g<v;g++){var y=new Date(t,e,g-a+1),k=!!B._isDate(this.date)&&B._compareDates(y,this.date),b=B._compareDates(y,s),w=-1!==n.events.indexOf(y.toDateString()),C=g<a||o+a<=g,E=g-a+1,M=e,O=t,x=n.startRange&&B._compareDates(n.startRange,y),L=n.endRange&&B._compareDates(n.endRange,y),T=n.startRange&&n.endRange&&n.startRange<y&&y<n.endRange;C&&(g<a?(E=p+E,M=h,O=u):(E-=o,M=d,O=c));var $={day:E,month:M,year:O,hasEvent:w,isSelected:k,isToday:b,isDisabled:n.minDate&&y<n.minDate||n.maxDate&&y>n.maxDate||n.disableWeekends&&B._isWeekend(y)||n.disableDayFn&&n.disableDayFn(y),isEmpty:C,isStartRange:x,isEndRange:L,isInRange:T,showDaysInNextAndPreviousMonths:n.showDaysInNextAndPreviousMonths};l.push(this.renderDay($)),7==++_&&(r.push(this.renderRow(l,n.isRTL,m)),_=0,m=!(l=[]))}return this.renderTable(n,r,i)}},{key:"renderDay",value:function(t){var e=[],i="false";if(t.isEmpty){if(!t.showDaysInNextAndPreviousMonths)return'<td class="is-empty"></td>';e.push("is-outside-current-month"),e.push("is-selection-disabled")}return t.isDisabled&&e.push("is-disabled"),t.isToday&&e.push("is-today"),t.isSelected&&(e.push("is-selected"),i="true"),t.hasEvent&&e.push("has-event"),t.isInRange&&e.push("is-inrange"),t.isStartRange&&e.push("is-startrange"),t.isEndRange&&e.push("is-endrange"),'<td data-day="'+t.day+'" class="'+e.join(" ")+'" aria-selected="'+i+'"><button class="datepicker-day-button" type="button" data-year="'+t.year+'" data-month="'+t.month+'" data-day="'+t.day+'">'+t.day+"</button></td>"}},{key:"renderRow",value:function(t,e,i){return'<tr class="datepicker-row'+(i?" is-selected":"")+'">'+(e?t.reverse():t).join("")+"</tr>"}},{key:"renderTable",value:function(t,e,i){return'<div class="datepicker-table-wrapper"><table cellpadding="0" cellspacing="0" class="datepicker-table" role="grid" aria-labelledby="'+i+'">'+this.renderHead(t)+this.renderBody(e)+"</table></div>"}},{key:"renderHead",value:function(t){var e=void 0,i=[];for(e=0;e<7;e++)i.push('<th scope="col"><abbr title="'+this.renderDayName(t,e)+'">'+this.renderDayName(t,e,!0)+"</abbr></th>");return"<thead><tr>"+(t.isRTL?i.reverse():i).join("")+"</tr></thead>"}},{key:"renderBody",value:function(t){return"<tbody>"+t.join("")+"</tbody>"}},{key:"renderTitle",value:function(t,e,i,n,s,o){var a,r,l=void 0,h=void 0,d=void 0,u=this.options,c=i===u.minYear,p=i===u.maxYear,v='<div id="'+o+'" class="datepicker-controls" role="heading" aria-live="assertive">',f=!0,m=!0;for(d=[],l=0;l<12;l++)d.push('<option value="'+(i===s?l-e:12+l-e)+'"'+(l===n?' selected="selected"':"")+(c&&l<u.minMonth||p&&l>u.maxMonth?'disabled="disabled"':"")+">"+u.i18n.months[l]+"</option>");for(a='<select class="datepicker-select orig-select-month" tabindex="-1">'+d.join("")+"</select>",g.isArray(u.yearRange)?(l=u.yearRange[0],h=u.yearRange[1]+1):(l=i-u.yearRange,h=1+i+u.yearRange),d=[];l<h&&l<=u.maxYear;l++)l>=u.minYear&&d.push('<option value="'+l+'" '+(l===i?'selected="selected"':"")+">"+l+"</option>");r='<select class="datepicker-select orig-select-year" tabindex="-1">'+d.join("")+"</select>";v+='<button class="month-prev'+(f?"":" is-disabled")+'" type="button"><svg fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M15.41 16.09l-4.58-4.59 4.58-4.59L14 5.5l-6 6 6 6z"/><path d="M0-.5h24v24H0z" fill="none"/></svg></button>',v+='<div class="selects-container">',u.showMonthAfterYear?v+=r+a:v+=a+r,v+="</div>",c&&(0===n||u.minMonth>=n)&&(f=!1),p&&(11===n||u.maxMonth<=n)&&(m=!1);return(v+='<button class="month-next'+(m?"":" is-disabled")+'" type="button"><svg fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M8.59 16.34l4.58-4.59-4.58-4.59L10 5.75l6 6-6 6z"/><path d="M0-.25h24v24H0z" fill="none"/></svg></button>')+"</div>"}},{key:"draw",value:function(t){if(this.isOpen||t){var e,i=this.options,n=i.minYear,s=i.maxYear,o=i.minMonth,a=i.maxMonth,r="";this._y<=n&&(this._y=n,!isNaN(o)&&this._m<o&&(this._m=o)),this._y>=s&&(this._y=s,!isNaN(a)&&this._m>a&&(this._m=a)),e="datepicker-title-"+Math.random().toString(36).replace(/[^a-z]+/g,"").substr(0,2);for(var l=0;l<1;l++)this._renderDateDisplay(),r+=this.renderTitle(this,l,this.calendars[l].year,this.calendars[l].month,this.calendars[0].year,e)+this.render(this.calendars[l].year,this.calendars[l].month,e);this.destroySelects(),this.calendarEl.innerHTML=r;var h=this.calendarEl.querySelector(".orig-select-year"),d=this.calendarEl.querySelector(".orig-select-month");M.FormSelect.init(h,{classes:"select-year",dropdownOptions:{container:document.body,constrainWidth:!1}}),M.FormSelect.init(d,{classes:"select-month",dropdownOptions:{container:document.body,constrainWidth:!1}}),h.addEventListener("change",this._handleYearChange.bind(this)),d.addEventListener("change",this._handleMonthChange.bind(this)),"function"==typeof this.options.onDraw&&this.options.onDraw(this)}}},{key:"_setupEventHandlers",value:function(){this._handleInputKeydownBound=this._handleInputKeydown.bind(this),this._handleInputClickBound=this._handleInputClick.bind(this),this._handleInputChangeBound=this._handleInputChange.bind(this),this._handleCalendarClickBound=this._handleCalendarClick.bind(this),this._finishSelectionBound=this._finishSelection.bind(this),this._handleMonthChange=this._handleMonthChange.bind(this),this._closeBound=this.close.bind(this),this.el.addEventListener("click",this._handleInputClickBound),this.el.addEventListener("keydown",this._handleInputKeydownBound),this.el.addEventListener("change",this._handleInputChangeBound),this.calendarEl.addEventListener("click",this._handleCalendarClickBound),this.doneBtn.addEventListener("click",this._finishSelectionBound),this.cancelBtn.addEventListener("click",this._closeBound),this.options.showClearBtn&&(this._handleClearClickBound=this._handleClearClick.bind(this),this.clearBtn.addEventListener("click",this._handleClearClickBound))}},{key:"_setupVariables",value:function(){var e=this;this.$modalEl=g(B._template),this.modalEl=this.$modalEl[0],this.calendarEl=this.modalEl.querySelector(".datepicker-calendar"),this.yearTextEl=this.modalEl.querySelector(".year-text"),this.dateTextEl=this.modalEl.querySelector(".date-text"),this.options.showClearBtn&&(this.clearBtn=this.modalEl.querySelector(".datepicker-clear")),this.doneBtn=this.modalEl.querySelector(".datepicker-done"),this.cancelBtn=this.modalEl.querySelector(".datepicker-cancel"),this.formats={d:function(){return e.date.getDate()},dd:function(){var t=e.date.getDate();return(t<10?"0":"")+t},ddd:function(){return e.options.i18n.weekdaysShort[e.date.getDay()]},dddd:function(){return e.options.i18n.weekdays[e.date.getDay()]},m:function(){return e.date.getMonth()+1},mm:function(){var t=e.date.getMonth()+1;return(t<10?"0":"")+t},mmm:function(){return e.options.i18n.monthsShort[e.date.getMonth()]},mmmm:function(){return e.options.i18n.months[e.date.getMonth()]},yy:function(){return(""+e.date.getFullYear()).slice(2)},yyyy:function(){return e.date.getFullYear()}}}},{key:"_removeEventHandlers",value:function(){this.el.removeEventListener("click",this._handleInputClickBound),this.el.removeEventListener("keydown",this._handleInputKeydownBound),this.el.removeEventListener("change",this._handleInputChangeBound),this.calendarEl.removeEventListener("click",this._handleCalendarClickBound)}},{key:"_handleInputClick",value:function(){this.open()}},{key:"_handleInputKeydown",value:function(t){t.which===M.keys.ENTER&&(t.preventDefault(),this.open())}},{key:"_handleCalendarClick",value:function(t){if(this.isOpen){var e=g(t.target);e.hasClass("is-disabled")||(!e.hasClass("datepicker-day-button")||e.hasClass("is-empty")||e.parent().hasClass("is-disabled")?e.closest(".month-prev").length?this.prevMonth():e.closest(".month-next").length&&this.nextMonth():(this.setDate(new Date(t.target.getAttribute("data-year"),t.target.getAttribute("data-month"),t.target.getAttribute("data-day"))),this.options.autoClose&&this._finishSelection()))}}},{key:"_handleClearClick",value:function(){this.date=null,this.setInputValue(),this.close()}},{key:"_handleMonthChange",value:function(t){this.gotoMonth(t.target.value)}},{key:"_handleYearChange",value:function(t){this.gotoYear(t.target.value)}},{key:"gotoMonth",value:function(t){isNaN(t)||(this.calendars[0].month=parseInt(t,10),this.adjustCalendars())}},{key:"gotoYear",value:function(t){isNaN(t)||(this.calendars[0].year=parseInt(t,10),this.adjustCalendars())}},{key:"_handleInputChange",value:function(t){var e=void 0;t.firedBy!==this&&(e=this.options.parse?this.options.parse(this.el.value,this.options.format):new Date(Date.parse(this.el.value)),B._isDate(e)&&this.setDate(e))}},{key:"renderDayName",value:function(t,e,i){for(e+=t.firstDay;7<=e;)e-=7;return i?t.i18n.weekdaysAbbrev[e]:t.i18n.weekdays[e]}},{key:"_finishSelection",value:function(){this.setInputValue(),this.close()}},{key:"open",value:function(){if(!this.isOpen)return this.isOpen=!0,"function"==typeof this.options.onOpen&&this.options.onOpen.call(this),this.draw(),this.modal.open(),this}},{key:"close",value:function(){if(this.isOpen)return this.isOpen=!1,"function"==typeof this.options.onClose&&this.options.onClose.call(this),this.modal.close(),this}}],[{key:"init",value:function(t,e){return _get(B.__proto__||Object.getPrototypeOf(B),"init",this).call(this,this,t,e)}},{key:"_isDate",value:function(t){return/Date/.test(Object.prototype.toString.call(t))&&!isNaN(t.getTime())}},{key:"_isWeekend",value:function(t){var e=t.getDay();return 0===e||6===e}},{key:"_setToStartOfDay",value:function(t){B._isDate(t)&&t.setHours(0,0,0,0)}},{key:"_getDaysInMonth",value:function(t,e){return[31,B._isLeapYear(t)?29:28,31,30,31,30,31,31,30,31,30,31][e]}},{key:"_isLeapYear",value:function(t){return t%4==0&&t%100!=0||t%400==0}},{key:"_compareDates",value:function(t,e){return t.getTime()===e.getTime()}},{key:"_setToStartOfDay",value:function(t){B._isDate(t)&&t.setHours(0,0,0,0)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Datepicker}},{key:"defaults",get:function(){return e}}]),B}();t._template=['<div class= "modal datepicker-modal">','<div class="modal-content datepicker-container">','<div class="datepicker-date-display">','<span class="year-text"></span>','<span class="date-text"></span>',"</div>",'<div class="datepicker-calendar-container">','<div class="datepicker-calendar"></div>','<div class="datepicker-footer">','<button class="btn-flat datepicker-clear waves-effect" style="visibility: hidden;" type="button"></button>','<div class="confirmation-btns">','<button class="btn-flat datepicker-cancel waves-effect" type="button"></button>','<button class="btn-flat datepicker-done waves-effect" type="button"></button>',"</div>","</div>","</div>","</div>","</div>"].join(""),M.Datepicker=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"datepicker","M_Datepicker")}(cash),function(h){"use strict";var e={dialRadius:135,outerRadius:105,innerRadius:70,tickRadius:20,duration:350,container:null,defaultTime:"now",fromNow:0,showClearBtn:!1,i18n:{cancel:"Cancel",clear:"Clear",done:"Ok"},autoClose:!1,twelveHour:!0,vibrate:!0,onOpenStart:null,onOpenEnd:null,onCloseStart:null,onCloseEnd:null,onSelect:null},t=function(t){function f(t,e){_classCallCheck(this,f);var i=_possibleConstructorReturn(this,(f.__proto__||Object.getPrototypeOf(f)).call(this,f,t,e));return(i.el.M_Timepicker=i).options=h.extend({},f.defaults,e),i.id=M.guid(),i._insertHTMLIntoDOM(),i._setupModal(),i._setupVariables(),i._setupEventHandlers(),i._clockSetup(),i._pickerSetup(),i}return _inherits(f,Component),_createClass(f,[{key:"destroy",value:function(){this._removeEventHandlers(),this.modal.destroy(),h(this.modalEl).remove(),this.el.M_Timepicker=void 0}},{key:"_setupEventHandlers",value:function(){this._handleInputKeydownBound=this._handleInputKeydown.bind(this),this._handleInputClickBound=this._handleInputClick.bind(this),this._handleClockClickStartBound=this._handleClockClickStart.bind(this),this._handleDocumentClickMoveBound=this._handleDocumentClickMove.bind(this),this._handleDocumentClickEndBound=this._handleDocumentClickEnd.bind(this),this.el.addEventListener("click",this._handleInputClickBound),this.el.addEventListener("keydown",this._handleInputKeydownBound),this.plate.addEventListener("mousedown",this._handleClockClickStartBound),this.plate.addEventListener("touchstart",this._handleClockClickStartBound),h(this.spanHours).on("click",this.showView.bind(this,"hours")),h(this.spanMinutes).on("click",this.showView.bind(this,"minutes"))}},{key:"_removeEventHandlers",value:function(){this.el.removeEventListener("click",this._handleInputClickBound),this.el.removeEventListener("keydown",this._handleInputKeydownBound)}},{key:"_handleInputClick",value:function(){this.open()}},{key:"_handleInputKeydown",value:function(t){t.which===M.keys.ENTER&&(t.preventDefault(),this.open())}},{key:"_handleClockClickStart",value:function(t){t.preventDefault();var e=this.plate.getBoundingClientRect(),i=e.left,n=e.top;this.x0=i+this.options.dialRadius,this.y0=n+this.options.dialRadius,this.moved=!1;var s=f._Pos(t);this.dx=s.x-this.x0,this.dy=s.y-this.y0,this.setHand(this.dx,this.dy,!1),document.addEventListener("mousemove",this._handleDocumentClickMoveBound),document.addEventListener("touchmove",this._handleDocumentClickMoveBound),document.addEventListener("mouseup",this._handleDocumentClickEndBound),document.addEventListener("touchend",this._handleDocumentClickEndBound)}},{key:"_handleDocumentClickMove",value:function(t){t.preventDefault();var e=f._Pos(t),i=e.x-this.x0,n=e.y-this.y0;this.moved=!0,this.setHand(i,n,!1,!0)}},{key:"_handleDocumentClickEnd",value:function(t){var e=this;t.preventDefault(),document.removeEventListener("mouseup",this._handleDocumentClickEndBound),document.removeEventListener("touchend",this._handleDocumentClickEndBound);var i=f._Pos(t),n=i.x-this.x0,s=i.y-this.y0;this.moved&&n===this.dx&&s===this.dy&&this.setHand(n,s),"hours"===this.currentView?this.showView("minutes",this.options.duration/2):this.options.autoClose&&(h(this.minutesView).addClass("timepicker-dial-out"),setTimeout(function(){e.done()},this.options.duration/2)),"function"==typeof this.options.onSelect&&this.options.onSelect.call(this,this.hours,this.minutes),document.removeEventListener("mousemove",this._handleDocumentClickMoveBound),document.removeEventListener("touchmove",this._handleDocumentClickMoveBound)}},{key:"_insertHTMLIntoDOM",value:function(){this.$modalEl=h(f._template),this.modalEl=this.$modalEl[0],this.modalEl.id="modal-"+this.id;var t=document.querySelector(this.options.container);this.options.container&&t?this.$modalEl.appendTo(t):this.$modalEl.insertBefore(this.el)}},{key:"_setupModal",value:function(){var t=this;this.modal=M.Modal.init(this.modalEl,{onOpenStart:this.options.onOpenStart,onOpenEnd:this.options.onOpenEnd,onCloseStart:this.options.onCloseStart,onCloseEnd:function(){"function"==typeof t.options.onCloseEnd&&t.options.onCloseEnd.call(t),t.isOpen=!1}})}},{key:"_setupVariables",value:function(){this.currentView="hours",this.vibrate=navigator.vibrate?"vibrate":navigator.webkitVibrate?"webkitVibrate":null,this._canvas=this.modalEl.querySelector(".timepicker-canvas"),this.plate=this.modalEl.querySelector(".timepicker-plate"),this.hoursView=this.modalEl.querySelector(".timepicker-hours"),this.minutesView=this.modalEl.querySelector(".timepicker-minutes"),this.spanHours=this.modalEl.querySelector(".timepicker-span-hours"),this.spanMinutes=this.modalEl.querySelector(".timepicker-span-minutes"),this.spanAmPm=this.modalEl.querySelector(".timepicker-span-am-pm"),this.footer=this.modalEl.querySelector(".timepicker-footer"),this.amOrPm="PM"}},{key:"_pickerSetup",value:function(){var t=h('<button class="btn-flat timepicker-clear waves-effect" style="visibility: hidden;" type="button" tabindex="'+(this.options.twelveHour?"3":"1")+'">'+this.options.i18n.clear+"</button>").appendTo(this.footer).on("click",this.clear.bind(this));this.options.showClearBtn&&t.css({visibility:""});var e=h('<div class="confirmation-btns"></div>');h('<button class="btn-flat timepicker-close waves-effect" type="button" tabindex="'+(this.options.twelveHour?"3":"1")+'">'+this.options.i18n.cancel+"</button>").appendTo(e).on("click",this.close.bind(this)),h('<button class="btn-flat timepicker-close waves-effect" type="button" tabindex="'+(this.options.twelveHour?"3":"1")+'">'+this.options.i18n.done+"</button>").appendTo(e).on("click",this.done.bind(this)),e.appendTo(this.footer)}},{key:"_clockSetup",value:function(){this.options.twelveHour&&(this.$amBtn=h('<div class="am-btn">AM</div>'),this.$pmBtn=h('<div class="pm-btn">PM</div>'),this.$amBtn.on("click",this._handleAmPmClick.bind(this)).appendTo(this.spanAmPm),this.$pmBtn.on("click",this._handleAmPmClick.bind(this)).appendTo(this.spanAmPm)),this._buildHoursView(),this._buildMinutesView(),this._buildSVGClock()}},{key:"_buildSVGClock",value:function(){var t=this.options.dialRadius,e=this.options.tickRadius,i=2*t,n=f._createSVGEl("svg");n.setAttribute("class","timepicker-svg"),n.setAttribute("width",i),n.setAttribute("height",i);var s=f._createSVGEl("g");s.setAttribute("transform","translate("+t+","+t+")");var o=f._createSVGEl("circle");o.setAttribute("class","timepicker-canvas-bearing"),o.setAttribute("cx",0),o.setAttribute("cy",0),o.setAttribute("r",4);var a=f._createSVGEl("line");a.setAttribute("x1",0),a.setAttribute("y1",0);var r=f._createSVGEl("circle");r.setAttribute("class","timepicker-canvas-bg"),r.setAttribute("r",e),s.appendChild(a),s.appendChild(r),s.appendChild(o),n.appendChild(s),this._canvas.appendChild(n),this.hand=a,this.bg=r,this.bearing=o,this.g=s}},{key:"_buildHoursView",value:function(){var t=h('<div class="timepicker-tick"></div>');if(this.options.twelveHour)for(var e=1;e<13;e+=1){var i=t.clone(),n=e/6*Math.PI,s=this.options.outerRadius;i.css({left:this.options.dialRadius+Math.sin(n)*s-this.options.tickRadius+"px",top:this.options.dialRadius-Math.cos(n)*s-this.options.tickRadius+"px"}),i.html(0===e?"00":e),this.hoursView.appendChild(i[0])}else for(var o=0;o<24;o+=1){var a=t.clone(),r=o/6*Math.PI,l=0<o&&o<13?this.options.innerRadius:this.options.outerRadius;a.css({left:this.options.dialRadius+Math.sin(r)*l-this.options.tickRadius+"px",top:this.options.dialRadius-Math.cos(r)*l-this.options.tickRadius+"px"}),a.html(0===o?"00":o),this.hoursView.appendChild(a[0])}}},{key:"_buildMinutesView",value:function(){for(var t=h('<div class="timepicker-tick"></div>'),e=0;e<60;e+=5){var i=t.clone(),n=e/30*Math.PI;i.css({left:this.options.dialRadius+Math.sin(n)*this.options.outerRadius-this.options.tickRadius+"px",top:this.options.dialRadius-Math.cos(n)*this.options.outerRadius-this.options.tickRadius+"px"}),i.html(f._addLeadingZero(e)),this.minutesView.appendChild(i[0])}}},{key:"_handleAmPmClick",value:function(t){var e=h(t.target);this.amOrPm=e.hasClass("am-btn")?"AM":"PM",this._updateAmPmView()}},{key:"_updateAmPmView",value:function(){this.options.twelveHour&&(this.$amBtn.toggleClass("text-primary","AM"===this.amOrPm),this.$pmBtn.toggleClass("text-primary","PM"===this.amOrPm))}},{key:"_updateTimeFromInput",value:function(){var t=((this.el.value||this.options.defaultTime||"")+"").split(":");if(this.options.twelveHour&&void 0!==t[1]&&(0<t[1].toUpperCase().indexOf("AM")?this.amOrPm="AM":this.amOrPm="PM",t[1]=t[1].replace("AM","").replace("PM","")),"now"===t[0]){var e=new Date(+new Date+this.options.fromNow);t=[e.getHours(),e.getMinutes()],this.options.twelveHour&&(this.amOrPm=12<=t[0]&&t[0]<24?"PM":"AM")}this.hours=+t[0]||0,this.minutes=+t[1]||0,this.spanHours.innerHTML=this.hours,this.spanMinutes.innerHTML=f._addLeadingZero(this.minutes),this._updateAmPmView()}},{key:"showView",value:function(t,e){"minutes"===t&&h(this.hoursView).css("visibility");var i="hours"===t,n=i?this.hoursView:this.minutesView,s=i?this.minutesView:this.hoursView;this.currentView=t,h(this.spanHours).toggleClass("text-primary",i),h(this.spanMinutes).toggleClass("text-primary",!i),s.classList.add("timepicker-dial-out"),h(n).css("visibility","visible").removeClass("timepicker-dial-out"),this.resetClock(e),clearTimeout(this.toggleViewTimer),this.toggleViewTimer=setTimeout(function(){h(s).css("visibility","hidden")},this.options.duration)}},{key:"resetClock",value:function(t){var e=this.currentView,i=this[e],n="hours"===e,s=i*(Math.PI/(n?6:30)),o=n&&0<i&&i<13?this.options.innerRadius:this.options.outerRadius,a=Math.sin(s)*o,r=-Math.cos(s)*o,l=this;t?(h(this.canvas).addClass("timepicker-canvas-out"),setTimeout(function(){h(l.canvas).removeClass("timepicker-canvas-out"),l.setHand(a,r)},t)):this.setHand(a,r)}},{key:"setHand",value:function(t,e,i){var n=this,s=Math.atan2(t,-e),o="hours"===this.currentView,a=Math.PI/(o||i?6:30),r=Math.sqrt(t*t+e*e),l=o&&r<(this.options.outerRadius+this.options.innerRadius)/2,h=l?this.options.innerRadius:this.options.outerRadius;this.options.twelveHour&&(h=this.options.outerRadius),s<0&&(s=2*Math.PI+s);var d=Math.round(s/a);s=d*a,this.options.twelveHour?o?0===d&&(d=12):(i&&(d*=5),60===d&&(d=0)):o?(12===d&&(d=0),d=l?0===d?12:d:0===d?0:d+12):(i&&(d*=5),60===d&&(d=0)),this[this.currentView]!==d&&this.vibrate&&this.options.vibrate&&(this.vibrateTimer||(navigator[this.vibrate](10),this.vibrateTimer=setTimeout(function(){n.vibrateTimer=null},100))),this[this.currentView]=d,o?this.spanHours.innerHTML=d:this.spanMinutes.innerHTML=f._addLeadingZero(d);var u=Math.sin(s)*(h-this.options.tickRadius),c=-Math.cos(s)*(h-this.options.tickRadius),p=Math.sin(s)*h,v=-Math.cos(s)*h;this.hand.setAttribute("x2",u),this.hand.setAttribute("y2",c),this.bg.setAttribute("cx",p),this.bg.setAttribute("cy",v)}},{key:"open",value:function(){this.isOpen||(this.isOpen=!0,this._updateTimeFromInput(),this.showView("hours"),this.modal.open())}},{key:"close",value:function(){this.isOpen&&(this.isOpen=!1,this.modal.close())}},{key:"done",value:function(t,e){var i=this.el.value,n=e?"":f._addLeadingZero(this.hours)+":"+f._addLeadingZero(this.minutes);this.time=n,!e&&this.options.twelveHour&&(n=n+" "+this.amOrPm),(this.el.value=n)!==i&&this.$el.trigger("change"),this.close(),this.el.focus()}},{key:"clear",value:function(){this.done(null,!0)}}],[{key:"init",value:function(t,e){return _get(f.__proto__||Object.getPrototypeOf(f),"init",this).call(this,this,t,e)}},{key:"_addLeadingZero",value:function(t){return(t<10?"0":"")+t}},{key:"_createSVGEl",value:function(t){return document.createElementNS("http://www.w3.org/2000/svg",t)}},{key:"_Pos",value:function(t){return t.targetTouches&&1<=t.targetTouches.length?{x:t.targetTouches[0].clientX,y:t.targetTouches[0].clientY}:{x:t.clientX,y:t.clientY}}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Timepicker}},{key:"defaults",get:function(){return e}}]),f}();t._template=['<div class= "modal timepicker-modal">','<div class="modal-content timepicker-container">','<div class="timepicker-digital-display">','<div class="timepicker-text-container">','<div class="timepicker-display-column">','<span class="timepicker-span-hours text-primary"></span>',":",'<span class="timepicker-span-minutes"></span>',"</div>",'<div class="timepicker-display-column timepicker-display-am-pm">','<div class="timepicker-span-am-pm"></div>',"</div>","</div>","</div>",'<div class="timepicker-analog-display">','<div class="timepicker-plate">','<div class="timepicker-canvas"></div>','<div class="timepicker-dial timepicker-hours"></div>','<div class="timepicker-dial timepicker-minutes timepicker-dial-out"></div>',"</div>",'<div class="timepicker-footer"></div>',"</div>","</div>","</div>"].join(""),M.Timepicker=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"timepicker","M_Timepicker")}(cash),function(s){"use strict";var e={},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return(i.el.M_CharacterCounter=i).options=s.extend({},n.defaults,e),i.isInvalid=!1,i.isValidLength=!1,i._setupCounter(),i._setupEventHandlers(),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){this._removeEventHandlers(),this.el.CharacterCounter=void 0,this._removeCounter()}},{key:"_setupEventHandlers",value:function(){this._handleUpdateCounterBound=this.updateCounter.bind(this),this.el.addEventListener("focus",this._handleUpdateCounterBound,!0),this.el.addEventListener("input",this._handleUpdateCounterBound,!0)}},{key:"_removeEventHandlers",value:function(){this.el.removeEventListener("focus",this._handleUpdateCounterBound,!0),this.el.removeEventListener("input",this._handleUpdateCounterBound,!0)}},{key:"_setupCounter",value:function(){this.counterEl=document.createElement("span"),s(this.counterEl).addClass("character-counter").css({float:"right","font-size":"12px",height:1}),this.$el.parent().append(this.counterEl)}},{key:"_removeCounter",value:function(){s(this.counterEl).remove()}},{key:"updateCounter",value:function(){var t=+this.$el.attr("data-length"),e=this.el.value.length;this.isValidLength=e<=t;var i=e;t&&(i+="/"+t,this._validateInput()),s(this.counterEl).html(i)}},{key:"_validateInput",value:function(){this.isValidLength&&this.isInvalid?(this.isInvalid=!1,this.$el.removeClass("invalid")):this.isValidLength||this.isInvalid||(this.isInvalid=!0,this.$el.removeClass("valid"),this.$el.addClass("invalid"))}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_CharacterCounter}},{key:"defaults",get:function(){return e}}]),n}();M.CharacterCounter=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"characterCounter","M_CharacterCounter")}(cash),function(b){"use strict";var e={duration:200,dist:-100,shift:0,padding:0,numVisible:5,fullWidth:!1,indicators:!1,noWrap:!1,onCycleTo:null},t=function(t){function i(t,e){_classCallCheck(this,i);var n=_possibleConstructorReturn(this,(i.__proto__||Object.getPrototypeOf(i)).call(this,i,t,e));return(n.el.M_Carousel=n).options=b.extend({},i.defaults,e),n.hasMultipleSlides=1<n.$el.find(".carousel-item").length,n.showIndicators=n.options.indicators&&n.hasMultipleSlides,n.noWrap=n.options.noWrap||!n.hasMultipleSlides,n.pressed=!1,n.dragged=!1,n.offset=n.target=0,n.images=[],n.itemWidth=n.$el.find(".carousel-item").first().innerWidth(),n.itemHeight=n.$el.find(".carousel-item").first().innerHeight(),n.dim=2*n.itemWidth+n.options.padding||1,n._autoScrollBound=n._autoScroll.bind(n),n._trackBound=n._track.bind(n),n.options.fullWidth&&(n.options.dist=0,n._setCarouselHeight(),n.showIndicators&&n.$el.find(".carousel-fixed-item").addClass("with-indicators")),n.$indicators=b('<ul class="indicators"></ul>'),n.$el.find(".carousel-item").each(function(t,e){if(n.images.push(t),n.showIndicators){var i=b('<li class="indicator-item"></li>');0===e&&i[0].classList.add("active"),n.$indicators.append(i)}}),n.showIndicators&&n.$el.append(n.$indicators),n.count=n.images.length,n.options.numVisible=Math.min(n.count,n.options.numVisible),n.xform="transform",["webkit","Moz","O","ms"].every(function(t){var e=t+"Transform";return void 0===document.body.style[e]||(n.xform=e,!1)}),n._setupEventHandlers(),n._scroll(n.offset),n}return _inherits(i,Component),_createClass(i,[{key:"destroy",value:function(){this._removeEventHandlers(),this.el.M_Carousel=void 0}},{key:"_setupEventHandlers",value:function(){var i=this;this._handleCarouselTapBound=this._handleCarouselTap.bind(this),this._handleCarouselDragBound=this._handleCarouselDrag.bind(this),this._handleCarouselReleaseBound=this._handleCarouselRelease.bind(this),this._handleCarouselClickBound=this._handleCarouselClick.bind(this),void 0!==window.ontouchstart&&(this.el.addEventListener("touchstart",this._handleCarouselTapBound),this.el.addEventListener("touchmove",this._handleCarouselDragBound),this.el.addEventListener("touchend",this._handleCarouselReleaseBound)),this.el.addEventListener("mousedown",this._handleCarouselTapBound),this.el.addEventListener("mousemove",this._handleCarouselDragBound),this.el.addEventListener("mouseup",this._handleCarouselReleaseBound),this.el.addEventListener("mouseleave",this._handleCarouselReleaseBound),this.el.addEventListener("click",this._handleCarouselClickBound),this.showIndicators&&this.$indicators&&(this._handleIndicatorClickBound=this._handleIndicatorClick.bind(this),this.$indicators.find(".indicator-item").each(function(t,e){t.addEventListener("click",i._handleIndicatorClickBound)}));var t=M.throttle(this._handleResize,200);this._handleThrottledResizeBound=t.bind(this),window.addEventListener("resize",this._handleThrottledResizeBound)}},{key:"_removeEventHandlers",value:function(){var i=this;void 0!==window.ontouchstart&&(this.el.removeEventListener("touchstart",this._handleCarouselTapBound),this.el.removeEventListener("touchmove",this._handleCarouselDragBound),this.el.removeEventListener("touchend",this._handleCarouselReleaseBound)),this.el.removeEventListener("mousedown",this._handleCarouselTapBound),this.el.removeEventListener("mousemove",this._handleCarouselDragBound),this.el.removeEventListener("mouseup",this._handleCarouselReleaseBound),this.el.removeEventListener("mouseleave",this._handleCarouselReleaseBound),this.el.removeEventListener("click",this._handleCarouselClickBound),this.showIndicators&&this.$indicators&&this.$indicators.find(".indicator-item").each(function(t,e){t.removeEventListener("click",i._handleIndicatorClickBound)}),window.removeEventListener("resize",this._handleThrottledResizeBound)}},{key:"_handleCarouselTap",value:function(t){"mousedown"===t.type&&b(t.target).is("img")&&t.preventDefault(),this.pressed=!0,this.dragged=!1,this.verticalDragged=!1,this.reference=this._xpos(t),this.referenceY=this._ypos(t),this.velocity=this.amplitude=0,this.frame=this.offset,this.timestamp=Date.now(),clearInterval(this.ticker),this.ticker=setInterval(this._trackBound,100)}},{key:"_handleCarouselDrag",value:function(t){var e=void 0,i=void 0,n=void 0;if(this.pressed)if(e=this._xpos(t),i=this._ypos(t),n=this.reference-e,Math.abs(this.referenceY-i)<30&&!this.verticalDragged)(2<n||n<-2)&&(this.dragged=!0,this.reference=e,this._scroll(this.offset+n));else{if(this.dragged)return t.preventDefault(),t.stopPropagation(),!1;this.verticalDragged=!0}if(this.dragged)return t.preventDefault(),t.stopPropagation(),!1}},{key:"_handleCarouselRelease",value:function(t){if(this.pressed)return this.pressed=!1,clearInterval(this.ticker),this.target=this.offset,(10<this.velocity||this.velocity<-10)&&(this.amplitude=.9*this.velocity,this.target=this.offset+this.amplitude),this.target=Math.round(this.target/this.dim)*this.dim,this.noWrap&&(this.target>=this.dim*(this.count-1)?this.target=this.dim*(this.count-1):this.target<0&&(this.target=0)),this.amplitude=this.target-this.offset,this.timestamp=Date.now(),requestAnimationFrame(this._autoScrollBound),this.dragged&&(t.preventDefault(),t.stopPropagation()),!1}},{key:"_handleCarouselClick",value:function(t){if(this.dragged)return t.preventDefault(),t.stopPropagation(),!1;if(!this.options.fullWidth){var e=b(t.target).closest(".carousel-item").index();0!==this._wrap(this.center)-e&&(t.preventDefault(),t.stopPropagation()),this._cycleTo(e)}}},{key:"_handleIndicatorClick",value:function(t){t.stopPropagation();var e=b(t.target).closest(".indicator-item");e.length&&this._cycleTo(e.index())}},{key:"_handleResize",value:function(t){this.options.fullWidth?(this.itemWidth=this.$el.find(".carousel-item").first().innerWidth(),this.imageHeight=this.$el.find(".carousel-item.active").height(),this.dim=2*this.itemWidth+this.options.padding,this.offset=2*this.center*this.itemWidth,this.target=this.offset,this._setCarouselHeight(!0)):this._scroll()}},{key:"_setCarouselHeight",value:function(t){var i=this,e=this.$el.find(".carousel-item.active").length?this.$el.find(".carousel-item.active").first():this.$el.find(".carousel-item").first(),n=e.find("img").first();if(n.length)if(n[0].complete){var s=n.height();if(0<s)this.$el.css("height",s+"px");else{var o=n[0].naturalWidth,a=n[0].naturalHeight,r=this.$el.width()/o*a;this.$el.css("height",r+"px")}}else n.one("load",function(t,e){i.$el.css("height",t.offsetHeight+"px")});else if(!t){var l=e.height();this.$el.css("height",l+"px")}}},{key:"_xpos",value:function(t){return t.targetTouches&&1<=t.targetTouches.length?t.targetTouches[0].clientX:t.clientX}},{key:"_ypos",value:function(t){return t.targetTouches&&1<=t.targetTouches.length?t.targetTouches[0].clientY:t.clientY}},{key:"_wrap",value:function(t){return t>=this.count?t%this.count:t<0?this._wrap(this.count+t%this.count):t}},{key:"_track",value:function(){var t,e,i,n;e=(t=Date.now())-this.timestamp,this.timestamp=t,i=this.offset-this.frame,this.frame=this.offset,n=1e3*i/(1+e),this.velocity=.8*n+.2*this.velocity}},{key:"_autoScroll",value:function(){var t=void 0,e=void 0;this.amplitude&&(t=Date.now()-this.timestamp,2<(e=this.amplitude*Math.exp(-t/this.options.duration))||e<-2?(this._scroll(this.target-e),requestAnimationFrame(this._autoScrollBound)):this._scroll(this.target))}},{key:"_scroll",value:function(t){var e=this;this.$el.hasClass("scrolling")||this.el.classList.add("scrolling"),null!=this.scrollingTimeout&&window.clearTimeout(this.scrollingTimeout),this.scrollingTimeout=window.setTimeout(function(){e.$el.removeClass("scrolling")},this.options.duration);var i,n,s,o,a=void 0,r=void 0,l=void 0,h=void 0,d=void 0,u=void 0,c=this.center,p=1/this.options.numVisible;if(this.offset="number"==typeof t?t:this.offset,this.center=Math.floor((this.offset+this.dim/2)/this.dim),o=-(s=(n=this.offset-this.center*this.dim)<0?1:-1)*n*2/this.dim,i=this.count>>1,this.options.fullWidth?(l="translateX(0)",u=1):(l="translateX("+(this.el.clientWidth-this.itemWidth)/2+"px) ",l+="translateY("+(this.el.clientHeight-this.itemHeight)/2+"px)",u=1-p*o),this.showIndicators){var v=this.center%this.count,f=this.$indicators.find(".indicator-item.active");f.index()!==v&&(f.removeClass("active"),this.$indicators.find(".indicator-item").eq(v)[0].classList.add("active"))}if(!this.noWrap||0<=this.center&&this.center<this.count){r=this.images[this._wrap(this.center)],b(r).hasClass("active")||(this.$el.find(".carousel-item").removeClass("active"),r.classList.add("active"));var m=l+" translateX("+-n/2+"px) translateX("+s*this.options.shift*o*a+"px) translateZ("+this.options.dist*o+"px)";this._updateItemStyle(r,u,0,m)}for(a=1;a<=i;++a){if(this.options.fullWidth?(h=this.options.dist,d=a===i&&n<0?1-o:1):(h=this.options.dist*(2*a+o*s),d=1-p*(2*a+o*s)),!this.noWrap||this.center+a<this.count){r=this.images[this._wrap(this.center+a)];var g=l+" translateX("+(this.options.shift+(this.dim*a-n)/2)+"px) translateZ("+h+"px)";this._updateItemStyle(r,d,-a,g)}if(this.options.fullWidth?(h=this.options.dist,d=a===i&&0<n?1-o:1):(h=this.options.dist*(2*a-o*s),d=1-p*(2*a-o*s)),!this.noWrap||0<=this.center-a){r=this.images[this._wrap(this.center-a)];var _=l+" translateX("+(-this.options.shift+(-this.dim*a-n)/2)+"px) translateZ("+h+"px)";this._updateItemStyle(r,d,-a,_)}}if(!this.noWrap||0<=this.center&&this.center<this.count){r=this.images[this._wrap(this.center)];var y=l+" translateX("+-n/2+"px) translateX("+s*this.options.shift*o+"px) translateZ("+this.options.dist*o+"px)";this._updateItemStyle(r,u,0,y)}var k=this.$el.find(".carousel-item").eq(this._wrap(this.center));c!==this.center&&"function"==typeof this.options.onCycleTo&&this.options.onCycleTo.call(this,k[0],this.dragged),"function"==typeof this.oneTimeCallback&&(this.oneTimeCallback.call(this,k[0],this.dragged),this.oneTimeCallback=null)}},{key:"_updateItemStyle",value:function(t,e,i,n){t.style[this.xform]=n,t.style.zIndex=i,t.style.opacity=e,t.style.visibility="visible"}},{key:"_cycleTo",value:function(t,e){var i=this.center%this.count-t;this.noWrap||(i<0?Math.abs(i+this.count)<Math.abs(i)&&(i+=this.count):0<i&&Math.abs(i-this.count)<i&&(i-=this.count)),this.target=this.dim*Math.round(this.offset/this.dim),i<0?this.target+=this.dim*Math.abs(i):0<i&&(this.target-=this.dim*i),"function"==typeof e&&(this.oneTimeCallback=e),this.offset!==this.target&&(this.amplitude=this.target-this.offset,this.timestamp=Date.now(),requestAnimationFrame(this._autoScrollBound))}},{key:"next",value:function(t){(void 0===t||isNaN(t))&&(t=1);var e=this.center+t;if(e>=this.count||e<0){if(this.noWrap)return;e=this._wrap(e)}this._cycleTo(e)}},{key:"prev",value:function(t){(void 0===t||isNaN(t))&&(t=1);var e=this.center-t;if(e>=this.count||e<0){if(this.noWrap)return;e=this._wrap(e)}this._cycleTo(e)}},{key:"set",value:function(t,e){if((void 0===t||isNaN(t))&&(t=0),t>this.count||t<0){if(this.noWrap)return;t=this._wrap(t)}this._cycleTo(t,e)}}],[{key:"init",value:function(t,e){return _get(i.__proto__||Object.getPrototypeOf(i),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Carousel}},{key:"defaults",get:function(){return e}}]),i}();M.Carousel=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"carousel","M_Carousel")}(cash),function(S){"use strict";var e={onOpen:void 0,onClose:void 0},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return(i.el.M_TapTarget=i).options=S.extend({},n.defaults,e),i.isOpen=!1,i.$origin=S("#"+i.$el.attr("mydata-target")),i._setup(),i._calculatePositioning(),i._setupEventHandlers(),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){this._removeEventHandlers(),this.el.TapTarget=void 0}},{key:"_setupEventHandlers",value:function(){this._handleDocumentClickBound=this._handleDocumentClick.bind(this),this._handleTargetClickBound=this._handleTargetClick.bind(this),this._handleOriginClickBound=this._handleOriginClick.bind(this),this.el.addEventListener("click",this._handleTargetClickBound),this.originEl.addEventListener("click",this._handleOriginClickBound);var t=M.throttle(this._handleResize,200);this._handleThrottledResizeBound=t.bind(this),window.addEventListener("resize",this._handleThrottledResizeBound)}},{key:"_removeEventHandlers",value:function(){this.el.removeEventListener("click",this._handleTargetClickBound),this.originEl.removeEventListener("click",this._handleOriginClickBound),window.removeEventListener("resize",this._handleThrottledResizeBound)}},{key:"_handleTargetClick",value:function(t){this.open()}},{key:"_handleOriginClick",value:function(t){this.close()}},{key:"_handleResize",value:function(t){this._calculatePositioning()}},{key:"_handleDocumentClick",value:function(t){S(t.target).closest(".tap-target-wrapper").length||(this.close(),t.preventDefault(),t.stopPropagation())}},{key:"_setup",value:function(){this.wrapper=this.$el.parent()[0],this.waveEl=S(this.wrapper).find(".tap-target-wave")[0],this.originEl=S(this.wrapper).find(".tap-target-origin")[0],this.contentEl=this.$el.find(".tap-target-content")[0],S(this.wrapper).hasClass(".tap-target-wrapper")||(this.wrapper=document.createElement("div"),this.wrapper.classList.add("tap-target-wrapper"),this.$el.before(S(this.wrapper)),this.wrapper.append(this.el)),this.contentEl||(this.contentEl=document.createElement("div"),this.contentEl.classList.add("tap-target-content"),this.$el.append(this.contentEl)),this.waveEl||(this.waveEl=document.createElement("div"),this.waveEl.classList.add("tap-target-wave"),this.originEl||(this.originEl=this.$origin.clone(!0,!0),this.originEl.addClass("tap-target-origin"),this.originEl.removeAttr("id"),this.originEl.removeAttr("style"),this.originEl=this.originEl[0],this.waveEl.append(this.originEl)),this.wrapper.append(this.waveEl))}},{key:"_calculatePositioning",value:function(){var t="fixed"===this.$origin.css("position");if(!t)for(var e=this.$origin.parents(),i=0;i<e.length&&!(t="fixed"==S(e[i]).css("position"));i++);var n=this.$origin.outerWidth(),s=this.$origin.outerHeight(),o=t?this.$origin.offset().top-M.getDocumentScrollTop():this.$origin.offset().top,a=t?this.$origin.offset().left-M.getDocumentScrollLeft():this.$origin.offset().left,r=window.innerWidth,l=window.innerHeight,h=r/2,d=l/2,u=a<=h,c=h<a,p=o<=d,v=d<o,f=.25*r<=a&&a<=.75*r,m=this.$el.outerWidth(),g=this.$el.outerHeight(),_=o+s/2-g/2,y=a+n/2-m/2,k=t?"fixed":"absolute",b=f?m:m/2+n,w=g/2,C=p?g/2:0,E=u&&!f?m/2-n:0,O=n,x=v?"bottom":"top",L=2*n,T=L,$=g/2-T/2,B=m/2-L/2,D={};D.top=p?_+"px":"",D.right=c?r-y-m+"px":"",D.bottom=v?l-_-g+"px":"",D.left=u?y+"px":"",D.position=k,S(this.wrapper).css(D),S(this.contentEl).css({width:b+"px",height:w+"px",top:C+"px",right:"0px",bottom:"0px",left:E+"px",padding:O+"px",verticalAlign:x}),S(this.waveEl).css({top:$+"px",left:B+"px",width:L+"px",height:T+"px"})}},{key:"open",value:function(){this.isOpen||("function"==typeof this.options.onOpen&&this.options.onOpen.call(this,this.$origin[0]),this.isOpen=!0,this.wrapper.classList.add("open"),document.body.addEventListener("click",this._handleDocumentClickBound,!0),document.body.addEventListener("touchend",this._handleDocumentClickBound))}},{key:"close",value:function(){this.isOpen&&("function"==typeof this.options.onClose&&this.options.onClose.call(this,this.$origin[0]),this.isOpen=!1,this.wrapper.classList.remove("open"),document.body.removeEventListener("click",this._handleDocumentClickBound,!0),document.body.removeEventListener("touchend",this._handleDocumentClickBound))}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_TapTarget}},{key:"defaults",get:function(){return e}}]),n}();M.TapTarget=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"tapTarget","M_TapTarget")}(cash),function(d){"use strict";var e={classes:"",dropdownOptions:{}},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return i.$el.hasClass("browser-default")?_possibleConstructorReturn(i):((i.el.M_FormSelect=i).options=d.extend({},n.defaults,e),i.isMultiple=i.$el.prop("multiple"),i.el.tabIndex=-1,i._keysSelected={},i._valueDict={},i._setupMyDropdown(),i._setupEventHandlers(),i)}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){this._removeEventHandlers(),this._removeMyDropdown(),this.el.M_FormSelect=void 0}},{key:"_setupEventHandlers",value:function(){var e=this;this._handleSelectChangeBound=this._handleSelectChange.bind(this),this._handleOptionClickBound=this._handleOptionClick.bind(this),this._handleInputClickBound=this._handleInputClick.bind(this),d(this.dropdownOptions).find("li:not(.optgroup)").each(function(t){t.addEventListener("click",e._handleOptionClickBound)}),this.el.addEventListener("change",this._handleSelectChangeBound),this.input.addEventListener("click",this._handleInputClickBound)}},{key:"_removeEventHandlers",value:function(){var e=this;d(this.dropdownOptions).find("li:not(.optgroup)").each(function(t){t.removeEventListener("click",e._handleOptionClickBound)}),this.el.removeEventListener("change",this._handleSelectChangeBound),this.input.removeEventListener("click",this._handleInputClickBound)}},{key:"_handleSelectChange",value:function(t){this._setValueToInput()}},{key:"_handleOptionClick",value:function(t){t.preventDefault();var e=d(t.target).closest("li")[0],i=e.id;if(!d(e).hasClass("disabled")&&!d(e).hasClass("optgroup")&&i.length){var n=!0;if(this.isMultiple){var s=d(this.dropdownOptions).find("li.disabled.selected");s.length&&(s.removeClass("selected"),s.find('input[type="checkbox"]').prop("checked",!1),this._toggleEntryFromArray(s[0].id)),n=this._toggleEntryFromArray(i)}else d(this.dropdownOptions).find("li").removeClass("selected"),d(e).toggleClass("selected",n);d(this._valueDict[i].el).prop("selected")!==n&&(d(this._valueDict[i].el).prop("selected",n),this.$el.trigger("change"))}t.stopPropagation()}},{key:"_handleInputClick",value:function(){this.dropdown&&this.dropdown.isOpen&&(this._setValueToInput(),this._setSelectedStates())}},{key:"_setupMyDropdown",value:function(){var n=this;this.wrapper=document.createElement("div"),d(this.wrapper).addClass("select-wrapper "+this.options.classes),this.$el.before(d(this.wrapper)),this.wrapper.appendChild(this.el),this.el.disabled&&this.wrapper.classList.add("disabled"),this.$selectOptions=this.$el.children("option, optgroup"),this.dropdownOptions=document.createElement("ul"),this.dropdownOptions.id="select-options-"+M.guid(),d(this.dropdownOptions).addClass("dropdown-content select-dropdown "+(this.isMultiple?"multiple-select-dropdown":"")),this.$selectOptions.length&&this.$selectOptions.each(function(t){if(d(t).is("option")){var e=void 0;e=n.isMultiple?n._appendOptionWithIcon(n.$el,t,"multiple"):n._appendOptionWithIcon(n.$el,t),n._addOptionToValueDict(t,e)}else if(d(t).is("optgroup")){var i=d(t).children("option");d(n.dropdownOptions).append(d('<li class="optgroup"><span>'+t.getAttribute("label")+"</span></li>")[0]),i.each(function(t){var e=n._appendOptionWithIcon(n.$el,t,"optgroup-option");n._addOptionToValueDict(t,e)})}}),this.$el.after(this.dropdownOptions),this.input=document.createElement("input"),d(this.input).addClass("select-dropdown hqtdropdown-trigger"),this.input.setAttribute("type","text"),this.input.setAttribute("readonly","true"),this.input.setAttribute("mydata-target",this.dropdownOptions.id),this.el.disabled&&d(this.input).prop("disabled","true"),this.$el.before(this.input),this._setValueToInput();var t=d('<svg class="caret" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>');if(this.$el.before(t[0]),!this.el.disabled){var e=d.extend({},this.options.dropdownOptions);e.onOpenEnd=function(t){var e=d(n.dropdownOptions).find(".selected").first();if(e.length&&(M.keyDown=!0,n.dropdown.focusedIndex=e.index(),n.dropdown._focusFocusedItem(),M.keyDown=!1,n.dropdown.isScrollable)){var i=e[0].getBoundingClientRect().top-n.dropdownOptions.getBoundingClientRect().top;i-=n.dropdownOptions.clientHeight/2,n.dropdownOptions.scrollTop=i}},this.isMultiple&&(e.closeOnClick=!1),this.dropdown=M.MyDropdown.init(this.input,e)}this._setSelectedStates()}},{key:"_addOptionToValueDict",value:function(t,e){var i=Object.keys(this._valueDict).length,n=this.dropdownOptions.id+i,s={};e.id=n,s.el=t,s.optionEl=e,this._valueDict[n]=s}},{key:"_removeMyDropdown",value:function(){d(this.wrapper).find(".caret").remove(),d(this.input).remove(),d(this.dropdownOptions).remove(),d(this.wrapper).before(this.$el),d(this.wrapper).remove()}},{key:"_appendOptionWithIcon",value:function(t,e,i){var n=e.disabled?"disabled ":"",s="optgroup-option"===i?"optgroup-option ":"",o=this.isMultiple?'<label><input type="checkbox"'+n+'"/><span>'+e.innerHTML+"</span></label>":e.innerHTML,a=d("<li></li>"),r=d("<span></span>");r.html(o),a.addClass(n+" "+s),a.append(r);var l=e.getAttribute("data-icon");if(l){var h=d('<img alt="" src="'+l+'">');a.prepend(h)}return d(this.dropdownOptions).append(a[0]),a[0]}},{key:"_toggleEntryFromArray",value:function(t){var e=!this._keysSelected.hasOwnProperty(t),i=d(this._valueDict[t].optionEl);return e?this._keysSelected[t]=!0:delete this._keysSelected[t],i.toggleClass("selected",e),i.find('input[type="checkbox"]').prop("checked",e),i.prop("selected",e),e}},{key:"_setValueToInput",value:function(){var i=[];if(this.$el.find("option").each(function(t){if(d(t).prop("selected")){var e=d(t).text();i.push(e)}}),!i.length){var t=this.$el.find("option:disabled").eq(0);t.length&&""===t[0].value&&i.push(t.text())}this.input.value=i.join(", ")}},{key:"_setSelectedStates",value:function(){for(var t in this._keysSelected={},this._valueDict){var e=this._valueDict[t],i=d(e.el).prop("selected");d(e.optionEl).find('input[type="checkbox"]').prop("checked",i),i?(this._activateOption(d(this.dropdownOptions),d(e.optionEl)),this._keysSelected[t]=!0):d(e.optionEl).removeClass("selected")}}},{key:"_activateOption",value:function(t,e){e&&(this.isMultiple||t.find("li.selected").removeClass("selected"),d(e).addClass("selected"))}},{key:"getSelectedValues",value:function(){var t=[];for(var e in this._keysSelected)t.push(this._valueDict[e].el.value);return t}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_FormSelect}},{key:"defaults",get:function(){return e}}]),n}();M.FormSelect=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"formSelect","M_FormSelect")}(cash),function(s,e){"use strict";var i={},t=function(t){function n(t,e){_classCallCheck(this,n);var i=_possibleConstructorReturn(this,(n.__proto__||Object.getPrototypeOf(n)).call(this,n,t,e));return(i.el.M_Range=i).options=s.extend({},n.defaults,e),i._mousedown=!1,i._setupThumb(),i._setupEventHandlers(),i}return _inherits(n,Component),_createClass(n,[{key:"destroy",value:function(){this._removeEventHandlers(),this._removeThumb(),this.el.M_Range=void 0}},{key:"_setupEventHandlers",value:function(){this._handleRangeChangeBound=this._handleRangeChange.bind(this),this._handleRangeMousedownTouchstartBound=this._handleRangeMousedownTouchstart.bind(this),this._handleRangeInputMousemoveTouchmoveBound=this._handleRangeInputMousemoveTouchmove.bind(this),this._handleRangeMouseupTouchendBound=this._handleRangeMouseupTouchend.bind(this),this._handleRangeBlurMouseoutTouchleaveBound=this._handleRangeBlurMouseoutTouchleave.bind(this),this.el.addEventListener("change",this._handleRangeChangeBound),this.el.addEventListener("mousedown",this._handleRangeMousedownTouchstartBound),this.el.addEventListener("touchstart",this._handleRangeMousedownTouchstartBound),this.el.addEventListener("input",this._handleRangeInputMousemoveTouchmoveBound),this.el.addEventListener("mousemove",this._handleRangeInputMousemoveTouchmoveBound),this.el.addEventListener("touchmove",this._handleRangeInputMousemoveTouchmoveBound),this.el.addEventListener("mouseup",this._handleRangeMouseupTouchendBound),this.el.addEventListener("touchend",this._handleRangeMouseupTouchendBound),this.el.addEventListener("blur",this._handleRangeBlurMouseoutTouchleaveBound),this.el.addEventListener("mouseout",this._handleRangeBlurMouseoutTouchleaveBound),this.el.addEventListener("touchleave",this._handleRangeBlurMouseoutTouchleaveBound)}},{key:"_removeEventHandlers",value:function(){this.el.removeEventListener("change",this._handleRangeChangeBound),this.el.removeEventListener("mousedown",this._handleRangeMousedownTouchstartBound),this.el.removeEventListener("touchstart",this._handleRangeMousedownTouchstartBound),this.el.removeEventListener("input",this._handleRangeInputMousemoveTouchmoveBound),this.el.removeEventListener("mousemove",this._handleRangeInputMousemoveTouchmoveBound),this.el.removeEventListener("touchmove",this._handleRangeInputMousemoveTouchmoveBound),this.el.removeEventListener("mouseup",this._handleRangeMouseupTouchendBound),this.el.removeEventListener("touchend",this._handleRangeMouseupTouchendBound),this.el.removeEventListener("blur",this._handleRangeBlurMouseoutTouchleaveBound),this.el.removeEventListener("mouseout",this._handleRangeBlurMouseoutTouchleaveBound),this.el.removeEventListener("touchleave",this._handleRangeBlurMouseoutTouchleaveBound)}},{key:"_handleRangeChange",value:function(){s(this.value).html(this.$el.val()),s(this.thumb).hasClass("active")||this._showRangeBubble();var t=this._calcRangeOffset();s(this.thumb).addClass("active").css("left",t+"px")}},{key:"_handleRangeMousedownTouchstart",value:function(t){if(s(this.value).html(this.$el.val()),this._mousedown=!0,this.$el.addClass("active"),s(this.thumb).hasClass("active")||this._showRangeBubble(),"input"!==t.type){var e=this._calcRangeOffset();s(this.thumb).addClass("active").css("left",e+"px")}}},{key:"_handleRangeInputMousemoveTouchmove",value:function(){if(this._mousedown){s(this.thumb).hasClass("active")||this._showRangeBubble();var t=this._calcRangeOffset();s(this.thumb).addClass("active").css("left",t+"px"),s(this.value).html(this.$el.val())}}},{key:"_handleRangeMouseupTouchend",value:function(){this._mousedown=!1,this.$el.removeClass("active")}},{key:"_handleRangeBlurMouseoutTouchleave",value:function(){if(!this._mousedown){var t=7+parseInt(this.$el.css("padding-left"))+"px";s(this.thumb).hasClass("active")&&(e.remove(this.thumb),e({targets:this.thumb,height:0,width:0,top:10,easing:"easeOutQuad",marginLeft:t,duration:100})),s(this.thumb).removeClass("active")}}},{key:"_setupThumb",value:function(){this.thumb=document.createElement("span"),this.value=document.createElement("span"),s(this.thumb).addClass("thumb"),s(this.value).addClass("value"),s(this.thumb).append(this.value),this.$el.after(this.thumb)}},{key:"_removeThumb",value:function(){s(this.thumb).remove()}},{key:"_showRangeBubble",value:function(){var t=-7+parseInt(s(this.thumb).parent().css("padding-left"))+"px";e.remove(this.thumb),e({targets:this.thumb,height:30,width:30,top:-30,marginLeft:t,duration:300,easing:"easeOutQuint"})}},{key:"_calcRangeOffset",value:function(){var t=this.$el.width()-15,e=parseFloat(this.$el.attr("max"))||100,i=parseFloat(this.$el.attr("min"))||0;return(parseFloat(this.$el.val())-i)/(e-i)*t}}],[{key:"init",value:function(t,e){return _get(n.__proto__||Object.getPrototypeOf(n),"init",this).call(this,this,t,e)}},{key:"getInstance",value:function(t){return(t.jquery?t[0]:t).M_Range}},{key:"defaults",get:function(){return i}}]),n}();M.Range=t,M.jQueryLoaded&&M.initializeJqueryWrapper(t,"range","M_Range"),t.init(s("input[type=range]"))}(cash,M.anime);
!function (t, e) { "object" == typeof exports && "undefined" != typeof module ? module.exports = e() : "function" == typeof define && define.amd ? define(e) : (t = t || self).uuidv4 = e() }(this, (function () { "use strict"; var t = "undefined" != typeof crypto && crypto.getRandomValues && crypto.getRandomValues.bind(crypto) || "undefined" != typeof msCrypto && "function" == typeof msCrypto.getRandomValues && msCrypto.getRandomValues.bind(msCrypto), e = new Uint8Array(16); function n() { if (!t) throw new Error("crypto.getRandomValues() not supported. See https://github.com/uuidjs/uuid#getrandomvalues-not-supported"); return t(e) } for (var o = [], r = 0; r < 256; ++r)o.push((r + 256).toString(16).substr(1)); return function (t, e, r) { "string" == typeof t && (e = "binary" === t ? new Uint8Array(16) : null, t = null); var u = (t = t || {}).random || (t.rng || n)(); if (u[6] = 15 & u[6] | 64, u[8] = 63 & u[8] | 128, e) { for (var i = r || 0, d = 0; d < 16; ++d)e[i + d] = u[d]; return e } return function (t, e) { var n = e || 0, r = o; return (r[t[n + 0]] + r[t[n + 1]] + r[t[n + 2]] + r[t[n + 3]] + "-" + r[t[n + 4]] + r[t[n + 5]] + "-" + r[t[n + 6]] + r[t[n + 7]] + "-" + r[t[n + 8]] + r[t[n + 9]] + "-" + r[t[n + 10]] + r[t[n + 11]] + r[t[n + 12]] + r[t[n + 13]] + r[t[n + 14]] + r[t[n + 15]]).toLowerCase() }(u) } }));
//
// uiid.min
!function (t, e) { "object" == typeof exports && "undefined" != typeof module ? module.exports = e() : "function" == typeof define && define.amd ? define(e) : (t = t || self).uuidv4 = e() }(this, (function () { "use strict"; var t = "undefined" != typeof crypto && crypto.getRandomValues && crypto.getRandomValues.bind(crypto) || "undefined" != typeof msCrypto && "function" == typeof msCrypto.getRandomValues && msCrypto.getRandomValues.bind(msCrypto), e = new Uint8Array(16); function n() { if (!t) throw new Error("crypto.getRandomValues() not supported. See https://github.com/uuidjs/uuid#getrandomvalues-not-supported"); return t(e) } for (var o = [], r = 0; r < 256; ++r)o.push((r + 256).toString(16).substr(1)); return function (t, e, r) { "string" == typeof t && (e = "binary" === t ? new Uint8Array(16) : null, t = null); var u = (t = t || {}).random || (t.rng || n)(); if (u[6] = 15 & u[6] | 64, u[8] = 63 & u[8] | 128, e) { for (var i = r || 0, d = 0; d < 16; ++d)e[i + d] = u[d]; return e } return function (t, e) { var n = e || 0, r = o; return (r[t[n + 0]] + r[t[n + 1]] + r[t[n + 2]] + r[t[n + 3]] + "-" + r[t[n + 4]] + r[t[n + 5]] + "-" + r[t[n + 6]] + r[t[n + 7]] + "-" + r[t[n + 8]] + r[t[n + 9]] + "-" + r[t[n + 10]] + r[t[n + 11]] + r[t[n + 12]] + r[t[n + 13]] + r[t[n + 14]] + r[t[n + 15]]).toLowerCase() }(u) } }));
//
/*! showdown v 1.9.1 - 02-11-2019 */
(function () { function e(e) { "use strict"; var r = { omitExtraWLInCodeBlocks: { defaultValue: !1, describe: "Omit the default extra whiteline added to code blocks", type: "boolean" }, noHeaderId: { defaultValue: !1, describe: "Turn on/off generated header id", type: "boolean" }, prefixHeaderId: { defaultValue: !1, describe: "Add a prefix to the generated header ids. Passing a string will prefix that string to the header id. Setting to true will add a generic 'section-' prefix", type: "string" }, rawPrefixHeaderId: { defaultValue: !1, describe: 'Setting this option to true will prevent showdown from modifying the prefix. This might result in malformed IDs (if, for instance, the " char is used in the prefix)', type: "boolean" }, ghCompatibleHeaderId: { defaultValue: !1, describe: "Generate header ids compatible with github style (spaces are replaced with dashes, a bunch of non alphanumeric chars are removed)", type: "boolean" }, rawHeaderId: { defaultValue: !1, describe: "Remove only spaces, ' and \" from generated header ids (including prefixes), replacing them with dashes (-). WARNING: This might result in malformed ids", type: "boolean" }, headerLevelStart: { defaultValue: !1, describe: "The header blocks level start", type: "integer" }, parseImgDimensions: { defaultValue: !1, describe: "Turn on/off image dimension parsing", type: "boolean" }, simplifiedAutoLink: { defaultValue: !1, describe: "Turn on/off GFM autolink style", type: "boolean" }, excludeTrailingPunctuationFromURLs: { defaultValue: !1, describe: "Excludes trailing punctuation from links generated with autoLinking", type: "boolean" }, literalMidWordUnderscores: { defaultValue: !1, describe: "Parse midword underscores as literal underscores", type: "boolean" }, literalMidWordAsterisks: { defaultValue: !1, describe: "Parse midword asterisks as literal asterisks", type: "boolean" }, strikethrough: { defaultValue: !1, describe: "Turn on/off strikethrough support", type: "boolean" }, tables: { defaultValue: !1, describe: "Turn on/off tables support", type: "boolean" }, tablesHeaderId: { defaultValue: !1, describe: "Add an id to table headers", type: "boolean" }, ghCodeBlocks: { defaultValue: !0, describe: "Turn on/off GFM fenced code blocks support", type: "boolean" }, tasklists: { defaultValue: !1, describe: "Turn on/off GFM tasklist support", type: "boolean" }, smoothLivePreview: { defaultValue: !1, describe: "Prevents weird effects in live previews due to incomplete input", type: "boolean" }, smartIndentationFix: { defaultValue: !1, description: "Tries to smartly fix indentation in es6 strings", type: "boolean" }, disableForced4SpacesIndentedSublists: { defaultValue: !1, description: "Disables the requirement of indenting nested sublists by 4 spaces", type: "boolean" }, simpleLineBreaks: { defaultValue: !1, description: "Parses simple line breaks as <br> (GFM Style)", type: "boolean" }, requireSpaceBeforeHeadingText: { defaultValue: !1, description: "Makes adding a space between `#` and the header text mandatory (GFM Style)", type: "boolean" }, ghMentions: { defaultValue: !1, description: "Enables github @mentions", type: "boolean" }, ghMentionsLink: { defaultValue: "https://github.com/{u}", description: "Changes the link generated by @mentions. Only applies if ghMentions option is enabled.", type: "string" }, encodeEmails: { defaultValue: !0, description: "Encode e-mail addresses through the use of Character Entities, transforming ASCII e-mail addresses into its equivalent decimal entities", type: "boolean" }, openLinksInNewWindow: { defaultValue: !1, description: "Open all links in new windows", type: "boolean" }, backslashEscapesHTMLTags: { defaultValue: !1, description: "Support for HTML Tag escaping. ex: <div>foo</div>", type: "boolean" }, emoji: { defaultValue: !1, description: "Enable emoji support. Ex: `this is a :smile: emoji`", type: "boolean" }, underline: { defaultValue: !1, description: "Enable support for underline. Syntax is double or triple underscores: `__underline word__`. With this option enabled, underscores no longer parses into `<em>` and `<strong>`", type: "boolean" }, completeHTMLDocument: { defaultValue: !1, description: "Outputs a complete html document, including `<html>`, `<head>` and `<body>` tags", type: "boolean" }, metadata: { defaultValue: !1, description: "Enable support for document metadata (defined at the top of the document between `«««` and `»»»` or between `---` and `---`).", type: "boolean" }, splitAdjacentBlockquotes: { defaultValue: !1, description: "Split adjacent blockquote blocks", type: "boolean" } }; if (!1 === e) return JSON.parse(JSON.stringify(r)); var t = {}; for (var a in r) r.hasOwnProperty(a) && (t[a] = r[a].defaultValue); return t } function r(e, r) { "use strict"; var t = r ? "Error in " + r + " extension->" : "Error in unnamed extension", n = { valid: !0, error: "" }; a.helper.isArray(e) || (e = [e]); for (var s = 0; s < e.length; ++s) { var o = t + " sub-extension " + s + ": ", i = e[s]; if ("object" != typeof i) return n.valid = !1, n.error = o + "must be an object, but " + typeof i + " given", n; if (!a.helper.isString(i.type)) return n.valid = !1, n.error = o + 'property "type" must be a string, but ' + typeof i.type + " given", n; var l = i.type = i.type.toLowerCase(); if ("language" === l && (l = i.type = "lang"), "html" === l && (l = i.type = "output"), "lang" !== l && "output" !== l && "listener" !== l) return n.valid = !1, n.error = o + "type " + l + ' is not recognized. Valid values: "lang/language", "output/html" or "listener"', n; if ("listener" === l) { if (a.helper.isUndefined(i.listeners)) return n.valid = !1, n.error = o + '. Extensions of type "listener" must have a property called "listeners"', n } else if (a.helper.isUndefined(i.filter) && a.helper.isUndefined(i.regex)) return n.valid = !1, n.error = o + l + ' extensions must define either a "regex" property or a "filter" method', n; if (i.listeners) { if ("object" != typeof i.listeners) return n.valid = !1, n.error = o + '"listeners" property must be an object but ' + typeof i.listeners + " given", n; for (var c in i.listeners) if (i.listeners.hasOwnProperty(c) && "function" != typeof i.listeners[c]) return n.valid = !1, n.error = o + '"listeners" property must be an hash of [event name]: [callback]. listeners.' + c + " must be a function but " + typeof i.listeners[c] + " given", n } if (i.filter) { if ("function" != typeof i.filter) return n.valid = !1, n.error = o + '"filter" must be a function, but ' + typeof i.filter + " given", n } else if (i.regex) { if (a.helper.isString(i.regex) && (i.regex = new RegExp(i.regex, "g")), !(i.regex instanceof RegExp)) return n.valid = !1, n.error = o + '"regex" property must either be a string or a RegExp object, but ' + typeof i.regex + " given", n; if (a.helper.isUndefined(i.replace)) return n.valid = !1, n.error = o + '"regex" extensions must implement a replace string or function', n } } return n } function t(e, r) { "use strict"; return "¨E" + r.charCodeAt(0) + "E" } var a = {}, n = {}, s = {}, o = e(!0), i = "vanilla", l = { github: { omitExtraWLInCodeBlocks: !0, simplifiedAutoLink: !0, excludeTrailingPunctuationFromURLs: !0, literalMidWordUnderscores: !0, strikethrough: !0, tables: !0, tablesHeaderId: !0, ghCodeBlocks: !0, tasklists: !0, disableForced4SpacesIndentedSublists: !0, simpleLineBreaks: !0, requireSpaceBeforeHeadingText: !0, ghCompatibleHeaderId: !0, ghMentions: !0, backslashEscapesHTMLTags: !0, emoji: !0, splitAdjacentBlockquotes: !0 }, original: { noHeaderId: !0, ghCodeBlocks: !1 }, ghost: { omitExtraWLInCodeBlocks: !0, parseImgDimensions: !0, simplifiedAutoLink: !0, excludeTrailingPunctuationFromURLs: !0, literalMidWordUnderscores: !0, strikethrough: !0, tables: !0, tablesHeaderId: !0, ghCodeBlocks: !0, tasklists: !0, smoothLivePreview: !0, simpleLineBreaks: !0, requireSpaceBeforeHeadingText: !0, ghMentions: !1, encodeEmails: !0 }, vanilla: e(!0), allOn: function () { "use strict"; var r = e(!0), t = {}; for (var a in r) r.hasOwnProperty(a) && (t[a] = !0); return t }() }; a.helper = {}, a.extensions = {}, a.setOption = function (e, r) { "use strict"; return o[e] = r, this }, a.getOption = function (e) { "use strict"; return o[e] }, a.getOptions = function () { "use strict"; return o }, a.resetOptions = function () { "use strict"; o = e(!0) }, a.setFlavor = function (e) { "use strict"; if (!l.hasOwnProperty(e)) throw Error(e + " flavor was not found"); a.resetOptions(); var r = l[e]; i = e; for (var t in r) r.hasOwnProperty(t) && (o[t] = r[t]) }, a.getFlavor = function () { "use strict"; return i }, a.getFlavorOptions = function (e) { "use strict"; if (l.hasOwnProperty(e)) return l[e] }, a.getDefaultOptions = function (r) { "use strict"; return e(r) }, a.subParser = function (e, r) { "use strict"; if (a.helper.isString(e)) { if (void 0 === r) { if (n.hasOwnProperty(e)) return n[e]; throw Error("SubParser named " + e + " not registered!") } n[e] = r } }, a.extension = function (e, t) { "use strict"; if (!a.helper.isString(e)) throw Error("Extension 'name' must be a string"); if (e = a.helper.stdExtName(e), a.helper.isUndefined(t)) { if (!s.hasOwnProperty(e)) throw Error("Extension named " + e + " is not registered!"); return s[e] } "function" == typeof t && (t = t()), a.helper.isArray(t) || (t = [t]); var n = r(t, e); if (!n.valid) throw Error(n.error); s[e] = t }, a.getAllExtensions = function () { "use strict"; return s }, a.removeExtension = function (e) { "use strict"; delete s[e] }, a.resetExtensions = function () { "use strict"; s = {} }, a.validateExtension = function (e) { "use strict"; var t = r(e, null); return !!t.valid || (console.warn(t.error), !1) }, a.hasOwnProperty("helper") || (a.helper = {}), a.helper.isString = function (e) { "use strict"; return "string" == typeof e || e instanceof String }, a.helper.isFunction = function (e) { "use strict"; return e && "[object Function]" === {}.toString.call(e) }, a.helper.isArray = function (e) { "use strict"; return Array.isArray(e) }, a.helper.isUndefined = function (e) { "use strict"; return void 0 === e }, a.helper.forEach = function (e, r) { "use strict"; if (a.helper.isUndefined(e)) throw new Error("obj param is required"); if (a.helper.isUndefined(r)) throw new Error("callback param is required"); if (!a.helper.isFunction(r)) throw new Error("callback param must be a function/closure"); if ("function" == typeof e.forEach) e.forEach(r); else if (a.helper.isArray(e)) for (var t = 0; t < e.length; t++)r(e[t], t, e); else { if ("object" != typeof e) throw new Error("obj does not seem to be an array or an iterable object"); for (var n in e) e.hasOwnProperty(n) && r(e[n], n, e) } }, a.helper.stdExtName = function (e) { "use strict"; return e.replace(/[_?*+\/\\.^-]/g, "").replace(/\s/g, "").toLowerCase() }, a.helper.escapeCharactersCallback = t, a.helper.escapeCharacters = function (e, r, a) { "use strict"; var n = "([" + r.replace(/([\[\]\\])/g, "\\$1") + "])"; a && (n = "\\\\" + n); var s = new RegExp(n, "g"); return e = e.replace(s, t) }, a.helper.unescapeHTMLEntities = function (e) { "use strict"; return e.replace(/&quot;/g, '"').replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&") }; var c = function (e, r, t, a) { "use strict"; var n, s, o, i, l, c = a || "", u = c.indexOf("g") > -1, d = new RegExp(r + "|" + t, "g" + c.replace(/g/g, "")), p = new RegExp(r, c.replace(/g/g, "")), h = []; do { for (n = 0; o = d.exec(e);)if (p.test(o[0])) n++ || (i = (s = d.lastIndex) - o[0].length); else if (n && !--n) { l = o.index + o[0].length; var _ = { left: { start: i, end: s }, match: { start: s, end: o.index }, right: { start: o.index, end: l }, wholeMatch: { start: i, end: l } }; if (h.push(_), !u) return h } } while (n && (d.lastIndex = s)); return h }; a.helper.matchRecursiveRegExp = function (e, r, t, a) { "use strict"; for (var n = c(e, r, t, a), s = [], o = 0; o < n.length; ++o)s.push([e.slice(n[o].wholeMatch.start, n[o].wholeMatch.end), e.slice(n[o].match.start, n[o].match.end), e.slice(n[o].left.start, n[o].left.end), e.slice(n[o].right.start, n[o].right.end)]); return s }, a.helper.replaceRecursiveRegExp = function (e, r, t, n, s) { "use strict"; if (!a.helper.isFunction(r)) { var o = r; r = function () { return o } } var i = c(e, t, n, s), l = e, u = i.length; if (u > 0) { var d = []; 0 !== i[0].wholeMatch.start && d.push(e.slice(0, i[0].wholeMatch.start)); for (var p = 0; p < u; ++p)d.push(r(e.slice(i[p].wholeMatch.start, i[p].wholeMatch.end), e.slice(i[p].match.start, i[p].match.end), e.slice(i[p].left.start, i[p].left.end), e.slice(i[p].right.start, i[p].right.end))), p < u - 1 && d.push(e.slice(i[p].wholeMatch.end, i[p + 1].wholeMatch.start)); i[u - 1].wholeMatch.end < e.length && d.push(e.slice(i[u - 1].wholeMatch.end)), l = d.join("") } return l }, a.helper.regexIndexOf = function (e, r, t) { "use strict"; if (!a.helper.isString(e)) throw "InvalidArgumentError: first parameter of showdown.helper.regexIndexOf function must be a string"; if (r instanceof RegExp == !1) throw "InvalidArgumentError: second parameter of showdown.helper.regexIndexOf function must be an instance of RegExp"; var n = e.substring(t || 0).search(r); return n >= 0 ? n + (t || 0) : n }, a.helper.splitAtIndex = function (e, r) { "use strict"; if (!a.helper.isString(e)) throw "InvalidArgumentError: first parameter of showdown.helper.regexIndexOf function must be a string"; return [e.substring(0, r), e.substring(r)] }, a.helper.encodeEmailAddress = function (e) { "use strict"; var r = [function (e) { return "&#" + e.charCodeAt(0) + ";" }, function (e) { return "&#x" + e.charCodeAt(0).toString(16) + ";" }, function (e) { return e }]; return e = e.replace(/./g, function (e) { if ("@" === e) e = r[Math.floor(2 * Math.random())](e); else { var t = Math.random(); e = t > .9 ? r[2](e) : t > .45 ? r[1](e) : r[0](e) } return e }) }, a.helper.padEnd = function (e, r, t) { "use strict"; return r >>= 0, t = String(t || " "), e.length > r ? String(e) : ((r -= e.length) > t.length && (t += t.repeat(r / t.length)), String(e) + t.slice(0, r)) }, "undefined" == typeof console && (console = { warn: function (e) { "use strict"; alert(e) }, log: function (e) { "use strict"; alert(e) }, error: function (e) { "use strict"; throw e } }), a.helper.regexes = { asteriskDashAndColon: /([*_:~])/g }, a.helper.emojis = { "+1": "👍", "-1": "👎", 100: "💯", 1234: "🔢", "1st_place_medal": "🥇", "2nd_place_medal": "🥈", "3rd_place_medal": "🥉", "8ball": "🎱", a: "🅰️", ab: "🆎", abc: "🔤", abcd: "🔡", accept: "🉑", aerial_tramway: "🚡", airplane: "✈️", alarm_clock: "⏰", alembic: "⚗️", alien: "👽", ambulance: "🚑", amphora: "🏺", anchor: "⚓️", angel: "👼", anger: "💢", angry: "😠", anguished: "😧", ant: "🐜", apple: "🍎", aquarius: "♒️", aries: "♈️", arrow_backward: "◀️", arrow_double_down: "⏬", arrow_double_up: "⏫", arrow_down: "⬇️", arrow_down_small: "🔽", arrow_forward: "▶️", arrow_heading_down: "⤵️", arrow_heading_up: "⤴️", arrow_left: "⬅️", arrow_lower_left: "↙️", arrow_lower_right: "↘️", arrow_right: "➡️", arrow_right_hook: "↪️", arrow_up: "⬆️", arrow_up_down: "↕️", arrow_up_small: "🔼", arrow_upper_left: "↖️", arrow_upper_right: "↗️", arrows_clockwise: "🔃", arrows_counterclockwise: "🔄", art: "🎨", articulated_lorry: "🚛", artificial_satellite: "🛰", astonished: "😲", athletic_shoe: "👟", atm: "🏧", atom_symbol: "⚛️", avocado: "🥑", b: "🅱️", baby: "👶", baby_bottle: "🍼", baby_chick: "🐤", baby_symbol: "🚼", back: "🔙", bacon: "🥓", badminton: "🏸", baggage_claim: "🛄", baguette_bread: "🥖", balance_scale: "⚖️", balloon: "🎈", ballot_box: "🗳", ballot_box_with_check: "☑️", bamboo: "🎍", banana: "🍌", bangbang: "‼️", bank: "🏦", bar_chart: "📊", barber: "💈", baseball: "⚾️", basketball: "🏀", basketball_man: "⛹️", basketball_woman: "⛹️&zwj;♀️", bat: "🦇", bath: "🛀", bathtub: "🛁", battery: "🔋", beach_umbrella: "🏖", bear: "🐻", bed: "🛏", bee: "🐝", beer: "🍺", beers: "🍻", beetle: "🐞", beginner: "🔰", bell: "🔔", bellhop_bell: "🛎", bento: "🍱", biking_man: "🚴", bike: "🚲", biking_woman: "🚴&zwj;♀️", bikini: "👙", biohazard: "☣️", bird: "🐦", birthday: "🎂", black_circle: "⚫️", black_flag: "🏴", black_heart: "🖤", black_joker: "🃏", black_large_square: "⬛️", black_medium_small_square: "◾️", black_medium_square: "◼️", black_nib: "✒️", black_small_square: "▪️", black_square_button: "🔲", blonde_man: "👱", blonde_woman: "👱&zwj;♀️", blossom: "🌼", blowfish: "🐡", blue_book: "📘", blue_car: "🚙", blue_heart: "💙", blush: "😊", boar: "🐗", boat: "⛵️", bomb: "💣", book: "📖", bookmark: "🔖", bookmark_tabs: "📑", books: "📚", boom: "💥", boot: "👢", bouquet: "💐", bowing_man: "🙇", bow_and_arrow: "🏹", bowing_woman: "🙇&zwj;♀️", bowling: "🎳", boxing_glove: "🥊", boy: "👦", bread: "🍞", bride_with_veil: "👰", bridge_at_night: "🌉", briefcase: "💼", broken_heart: "💔", bug: "🐛", building_construction: "🏗", bulb: "💡", bullettrain_front: "🚅", bullettrain_side: "🚄", burrito: "🌯", bus: "🚌", business_suit_levitating: "🕴", busstop: "🚏", bust_in_silhouette: "👤", busts_in_silhouette: "👥", butterfly: "🦋", cactus: "🌵", cake: "🍰", calendar: "📆", call_me_hand: "🤙", calling: "📲", camel: "🐫", camera: "📷", camera_flash: "📸", camping: "🏕", cancer: "♋️", candle: "🕯", candy: "🍬", canoe: "🛶", capital_abcd: "🔠", capricorn: "♑️", car: "🚗", card_file_box: "🗃", card_index: "📇", card_index_dividers: "🗂", carousel_horse: "🎠", carrot: "🥕", cat: "🐱", cat2: "🐈", cd: "💿", chains: "⛓", champagne: "🍾", chart: "💹", chart_with_downwards_trend: "📉", chart_with_upwards_trend: "📈", checkered_flag: "🏁", cheese: "🧀", cherries: "🍒", cherry_blossom: "🌸", chestnut: "🌰", chicken: "🐔", children_crossing: "🚸", chipmunk: "🐿", chocolate_bar: "🍫", christmas_tree: "🎄", church: "⛪️", cinema: "🎦", circus_tent: "🎪", city_sunrise: "🌇", city_sunset: "🌆", cityscape: "🏙", cl: "🆑", clamp: "🗜", clap: "👏", clapper: "🎬", classical_building: "🏛", clinking_glasses: "🥂", clipboard: "📋", clock1: "🕐", clock10: "🕙", clock1030: "🕥", clock11: "🕚", clock1130: "🕦", clock12: "🕛", clock1230: "🕧", clock130: "🕜", clock2: "🕑", clock230: "🕝", clock3: "🕒", clock330: "🕞", clock4: "🕓", clock430: "🕟", clock5: "🕔", clock530: "🕠", clock6: "🕕", clock630: "🕡", clock7: "🕖", clock730: "🕢", clock8: "🕗", clock830: "🕣", clock9: "🕘", clock930: "🕤", closed_book: "📕", closed_lock_with_key: "🔐", closed_umbrella: "🌂", cloud: "☁️", cloud_with_lightning: "🌩", cloud_with_lightning_and_rain: "⛈", cloud_with_rain: "🌧", cloud_with_snow: "🌨", clown_face: "🤡", clubs: "♣️", cocktail: "🍸", coffee: "☕️", coffin: "⚰️", cold_sweat: "😰", comet: "☄️", computer: "💻", computer_mouse: "🖱", confetti_ball: "🎊", confounded: "😖", confused: "😕", congratulations: "㊗️", construction: "🚧", construction_worker_man: "👷", construction_worker_woman: "👷&zwj;♀️", control_knobs: "🎛", convenience_store: "🏪", cookie: "🍪", cool: "🆒", policeman: "👮", copyright: "©️", corn: "🌽", couch_and_lamp: "🛋", couple: "👫", couple_with_heart_woman_man: "💑", couple_with_heart_man_man: "👨&zwj;❤️&zwj;👨", couple_with_heart_woman_woman: "👩&zwj;❤️&zwj;👩", couplekiss_man_man: "👨&zwj;❤️&zwj;💋&zwj;👨", couplekiss_man_woman: "💏", couplekiss_woman_woman: "👩&zwj;❤️&zwj;💋&zwj;👩", cow: "🐮", cow2: "🐄", cowboy_hat_face: "🤠", crab: "🦀", crayon: "🖍", credit_card: "💳", crescent_moon: "🌙", cricket: "🏏", crocodile: "🐊", croissant: "🥐", crossed_fingers: "🤞", crossed_flags: "🎌", crossed_swords: "⚔️", crown: "👑", cry: "😢", crying_cat_face: "😿", crystal_ball: "🔮", cucumber: "🥒", cupid: "💘", curly_loop: "➰", currency_exchange: "💱", curry: "🍛", custard: "🍮", customs: "🛃", cyclone: "🌀", dagger: "🗡", dancer: "💃", dancing_women: "👯", dancing_men: "👯&zwj;♂️", dango: "🍡", dark_sunglasses: "🕶", dart: "🎯", dash: "💨", date: "📅", deciduous_tree: "🌳", deer: "🦌", department_store: "🏬", derelict_house: "🏚", desert: "🏜", desert_island: "🏝", desktop_computer: "🖥", male_detective: "🕵️", diamond_shape_with_a_dot_inside: "💠", diamonds: "♦️", disappointed: "😞", disappointed_relieved: "😥", dizzy: "💫", dizzy_face: "😵", do_not_litter: "🚯", dog: "🐶", dog2: "🐕", dollar: "💵", dolls: "🎎", dolphin: "🐬", door: "🚪", doughnut: "🍩", dove: "🕊", dragon: "🐉", dragon_face: "🐲", dress: "👗", dromedary_camel: "🐪", drooling_face: "🤤", droplet: "💧", drum: "🥁", duck: "🦆", dvd: "📀", "e-mail": "📧", eagle: "🦅", ear: "👂", ear_of_rice: "🌾", earth_africa: "🌍", earth_americas: "🌎", earth_asia: "🌏", egg: "🥚", eggplant: "🍆", eight_pointed_black_star: "✴️", eight_spoked_asterisk: "✳️", electric_plug: "🔌", elephant: "🐘", email: "✉️", end: "🔚", envelope_with_arrow: "📩", euro: "💶", european_castle: "🏰", european_post_office: "🏤", evergreen_tree: "🌲", exclamation: "❗️", expressionless: "😑", eye: "👁", eye_speech_bubble: "👁&zwj;🗨", eyeglasses: "👓", eyes: "👀", face_with_head_bandage: "🤕", face_with_thermometer: "🤒", fist_oncoming: "👊", factory: "🏭", fallen_leaf: "🍂", family_man_woman_boy: "👪", family_man_boy: "👨&zwj;👦", family_man_boy_boy: "👨&zwj;👦&zwj;👦", family_man_girl: "👨&zwj;👧", family_man_girl_boy: "👨&zwj;👧&zwj;👦", family_man_girl_girl: "👨&zwj;👧&zwj;👧", family_man_man_boy: "👨&zwj;👨&zwj;👦", family_man_man_boy_boy: "👨&zwj;👨&zwj;👦&zwj;👦", family_man_man_girl: "👨&zwj;👨&zwj;👧", family_man_man_girl_boy: "👨&zwj;👨&zwj;👧&zwj;👦", family_man_man_girl_girl: "👨&zwj;👨&zwj;👧&zwj;👧", family_man_woman_boy_boy: "👨&zwj;👩&zwj;👦&zwj;👦", family_man_woman_girl: "👨&zwj;👩&zwj;👧", family_man_woman_girl_boy: "👨&zwj;👩&zwj;👧&zwj;👦", family_man_woman_girl_girl: "👨&zwj;👩&zwj;👧&zwj;👧", family_woman_boy: "👩&zwj;👦", family_woman_boy_boy: "👩&zwj;👦&zwj;👦", family_woman_girl: "👩&zwj;👧", family_woman_girl_boy: "👩&zwj;👧&zwj;👦", family_woman_girl_girl: "👩&zwj;👧&zwj;👧", family_woman_woman_boy: "👩&zwj;👩&zwj;👦", family_woman_woman_boy_boy: "👩&zwj;👩&zwj;👦&zwj;👦", family_woman_woman_girl: "👩&zwj;👩&zwj;👧", family_woman_woman_girl_boy: "👩&zwj;👩&zwj;👧&zwj;👦", family_woman_woman_girl_girl: "👩&zwj;👩&zwj;👧&zwj;👧", fast_forward: "⏩", fax: "📠", fearful: "😨", feet: "🐾", female_detective: "🕵️&zwj;♀️", ferris_wheel: "🎡", ferry: "⛴", field_hockey: "🏑", file_cabinet: "🗄", file_folder: "📁", film_projector: "📽", film_strip: "🎞", fire: "🔥", fire_engine: "🚒", fireworks: "🎆", first_quarter_moon: "🌓", first_quarter_moon_with_face: "🌛", fish: "🐟", fish_cake: "🍥", fishing_pole_and_fish: "🎣", fist_raised: "✊", fist_left: "🤛", fist_right: "🤜", flags: "🎏", flashlight: "🔦", fleur_de_lis: "⚜️", flight_arrival: "🛬", flight_departure: "🛫", floppy_disk: "💾", flower_playing_cards: "🎴", flushed: "😳", fog: "🌫", foggy: "🌁", football: "🏈", footprints: "👣", fork_and_knife: "🍴", fountain: "⛲️", fountain_pen: "🖋", four_leaf_clover: "🍀", fox_face: "🦊", framed_picture: "🖼", free: "🆓", fried_egg: "🍳", fried_shrimp: "🍤", fries: "🍟", frog: "🐸", frowning: "😦", frowning_face: "☹️", frowning_man: "🙍&zwj;♂️", frowning_woman: "🙍", middle_finger: "🖕", fuelpump: "⛽️", full_moon: "🌕", full_moon_with_face: "🌝", funeral_urn: "⚱️", game_die: "🎲", gear: "⚙️", gem: "💎", gemini: "♊️", ghost: "👻", gift: "🎁", gift_heart: "💝", girl: "👧", globe_with_meridians: "🌐", goal_net: "🥅", goat: "🐐", golf: "⛳️", golfing_man: "🏌️", golfing_woman: "🏌️&zwj;♀️", gorilla: "🦍", grapes: "🍇", green_apple: "🍏", green_book: "📗", green_heart: "💚", green_salad: "🥗", grey_exclamation: "❕", grey_question: "❔", grimacing: "😬", grin: "😁", grinning: "😀", guardsman: "💂", guardswoman: "💂&zwj;♀️", guitar: "🎸", gun: "🔫", haircut_woman: "💇", haircut_man: "💇&zwj;♂️", hamburger: "🍔", hammer: "🔨", hammer_and_pick: "⚒", hammer_and_wrench: "🛠", hamster: "🐹", hand: "✋", handbag: "👜", handshake: "🤝", hankey: "💩", hatched_chick: "🐥", hatching_chick: "🐣", headphones: "🎧", hear_no_evil: "🙉", heart: "❤️", heart_decoration: "💟", heart_eyes: "😍", heart_eyes_cat: "😻", heartbeat: "💓", heartpulse: "💗", hearts: "♥️", heavy_check_mark: "✔️", heavy_division_sign: "➗", heavy_dollar_sign: "💲", heavy_heart_exclamation: "❣️", heavy_minus_sign: "➖", heavy_multiplication_x: "✖️", heavy_plus_sign: "➕", helicopter: "🚁", herb: "🌿", hibiscus: "🌺", high_brightness: "🔆", high_heel: "👠", hocho: "🔪", hole: "🕳", honey_pot: "🍯", horse: "🐴", horse_racing: "🏇", hospital: "🏥", hot_pepper: "🌶", hotdog: "🌭", hotel: "🏨", hotsprings: "♨️", hourglass: "⌛️", hourglass_flowing_sand: "⏳", house: "🏠", house_with_garden: "🏡", houses: "🏘", hugs: "🤗", hushed: "😯", ice_cream: "🍨", ice_hockey: "🏒", ice_skate: "⛸", icecream: "🍦", id: "🆔", ideograph_advantage: "🉐", imp: "👿", inbox_tray: "📥", incoming_envelope: "📨", tipping_hand_woman: "💁", information_source: "ℹ️", innocent: "😇", interrobang: "⁉️", iphone: "📱", izakaya_lantern: "🏮", jack_o_lantern: "🎃", japan: "🗾", japanese_castle: "🏯", japanese_goblin: "👺", japanese_ogre: "👹", jeans: "👖", joy: "😂", joy_cat: "😹", joystick: "🕹", kaaba: "🕋", key: "🔑", keyboard: "⌨️", keycap_ten: "🔟", kick_scooter: "🛴", kimono: "👘", kiss: "💋", kissing: "😗", kissing_cat: "😽", kissing_closed_eyes: "😚", kissing_heart: "😘", kissing_smiling_eyes: "😙", kiwi_fruit: "🥝", koala: "🐨", koko: "🈁", label: "🏷", large_blue_circle: "🔵", large_blue_diamond: "🔷", large_orange_diamond: "🔶", last_quarter_moon: "🌗", last_quarter_moon_with_face: "🌜", latin_cross: "✝️", laughing: "😆", leaves: "🍃", ledger: "📒", left_luggage: "🛅", left_right_arrow: "↔️", leftwards_arrow_with_hook: "↩️", lemon: "🍋", leo: "♌️", leopard: "🐆", level_slider: "🎚", libra: "♎️", light_rail: "🚈", link: "🔗", lion: "🦁", lips: "👄", lipstick: "💄", lizard: "🦎", lock: "🔒", lock_with_ink_pen: "🔏", lollipop: "🍭", loop: "➿", loud_sound: "🔊", loudspeaker: "📢", love_hotel: "🏩", love_letter: "💌", low_brightness: "🔅", lying_face: "🤥", m: "Ⓜ️", mag: "🔍", mag_right: "🔎", mahjong: "🀄️", mailbox: "📫", mailbox_closed: "📪", mailbox_with_mail: "📬", mailbox_with_no_mail: "📭", man: "👨", man_artist: "👨&zwj;🎨", man_astronaut: "👨&zwj;🚀", man_cartwheeling: "🤸&zwj;♂️", man_cook: "👨&zwj;🍳", man_dancing: "🕺", man_facepalming: "🤦&zwj;♂️", man_factory_worker: "👨&zwj;🏭", man_farmer: "👨&zwj;🌾", man_firefighter: "👨&zwj;🚒", man_health_worker: "👨&zwj;⚕️", man_in_tuxedo: "🤵", man_judge: "👨&zwj;⚖️", man_juggling: "🤹&zwj;♂️", man_mechanic: "👨&zwj;🔧", man_office_worker: "👨&zwj;💼", man_pilot: "👨&zwj;✈️", man_playing_handball: "🤾&zwj;♂️", man_playing_water_polo: "🤽&zwj;♂️", man_scientist: "👨&zwj;🔬", man_shrugging: "🤷&zwj;♂️", man_singer: "👨&zwj;🎤", man_student: "👨&zwj;🎓", man_teacher: "👨&zwj;🏫", man_technologist: "👨&zwj;💻", man_with_gua_pi_mao: "👲", man_with_turban: "👳", tangerine: "🍊", mans_shoe: "👞", mantelpiece_clock: "🕰", maple_leaf: "🍁", martial_arts_uniform: "🥋", mask: "😷", massage_woman: "💆", massage_man: "💆&zwj;♂️", meat_on_bone: "🍖", medal_military: "🎖", medal_sports: "🏅", mega: "📣", melon: "🍈", memo: "📝", men_wrestling: "🤼&zwj;♂️", menorah: "🕎", mens: "🚹", metal: "🤘", metro: "🚇", microphone: "🎤", microscope: "🔬", milk_glass: "🥛", milky_way: "🌌", minibus: "🚐", minidisc: "💽", mobile_phone_off: "📴", money_mouth_face: "🤑", money_with_wings: "💸", moneybag: "💰", monkey: "🐒", monkey_face: "🐵", monorail: "🚝", moon: "🌔", mortar_board: "🎓", mosque: "🕌", motor_boat: "🛥", motor_scooter: "🛵", motorcycle: "🏍", motorway: "🛣", mount_fuji: "🗻", mountain: "⛰", mountain_biking_man: "🚵", mountain_biking_woman: "🚵&zwj;♀️", mountain_cableway: "🚠", mountain_railway: "🚞", mountain_snow: "🏔", mouse: "🐭", mouse2: "🐁", movie_camera: "🎥", moyai: "🗿", mrs_claus: "🤶", muscle: "💪", mushroom: "🍄", musical_keyboard: "🎹", musical_note: "🎵", musical_score: "🎼", mute: "🔇", nail_care: "💅", name_badge: "📛", national_park: "🏞", nauseated_face: "🤢", necktie: "👔", negative_squared_cross_mark: "❎", nerd_face: "🤓", neutral_face: "😐", new: "🆕", new_moon: "🌑", new_moon_with_face: "🌚", newspaper: "📰", newspaper_roll: "🗞", next_track_button: "⏭", ng: "🆖", no_good_man: "🙅&zwj;♂️", no_good_woman: "🙅", night_with_stars: "🌃", no_bell: "🔕", no_bicycles: "🚳", no_entry: "⛔️", no_entry_sign: "🚫", no_mobile_phones: "📵", no_mouth: "😶", no_pedestrians: "🚷", no_smoking: "🚭", "non-potable_water": "🚱", nose: "👃", notebook: "📓", notebook_with_decorative_cover: "📔", notes: "🎶", nut_and_bolt: "🔩", o: "⭕️", o2: "🅾️", ocean: "🌊", octopus: "🐙", oden: "🍢", office: "🏢", oil_drum: "🛢", ok: "🆗", ok_hand: "👌", ok_man: "🙆&zwj;♂️", ok_woman: "🙆", old_key: "🗝", older_man: "👴", older_woman: "👵", om: "🕉", on: "🔛", oncoming_automobile: "🚘", oncoming_bus: "🚍", oncoming_police_car: "🚔", oncoming_taxi: "🚖", open_file_folder: "📂", open_hands: "👐", open_mouth: "😮", open_umbrella: "☂️", ophiuchus: "⛎", orange_book: "📙", orthodox_cross: "☦️", outbox_tray: "📤", owl: "🦉", ox: "🐂", package: "📦", page_facing_up: "📄", page_with_curl: "📃", pager: "📟", paintbrush: "🖌", palm_tree: "🌴", pancakes: "🥞", panda_face: "🐼", paperclip: "📎", paperclips: "🖇", parasol_on_ground: "⛱", parking: "🅿️", part_alternation_mark: "〽️", partly_sunny: "⛅️", passenger_ship: "🛳", passport_control: "🛂", pause_button: "⏸", peace_symbol: "☮️", peach: "🍑", peanuts: "🥜", pear: "🍐", pen: "🖊", pencil2: "✏️", penguin: "🐧", pensive: "😔", performing_arts: "🎭", persevere: "😣", person_fencing: "🤺", pouting_woman: "🙎", phone: "☎️", pick: "⛏", pig: "🐷", pig2: "🐖", pig_nose: "🐽", pill: "💊", pineapple: "🍍", ping_pong: "🏓", pisces: "♓️", pizza: "🍕", place_of_worship: "🛐", plate_with_cutlery: "🍽", play_or_pause_button: "⏯", point_down: "👇", point_left: "👈", point_right: "👉", point_up: "☝️", point_up_2: "👆", police_car: "🚓", policewoman: "👮&zwj;♀️", poodle: "🐩", popcorn: "🍿", post_office: "🏣", postal_horn: "📯", postbox: "📮", potable_water: "🚰", potato: "🥔", pouch: "👝", poultry_leg: "🍗", pound: "💷", rage: "😡", pouting_cat: "😾", pouting_man: "🙎&zwj;♂️", pray: "🙏", prayer_beads: "📿", pregnant_woman: "🤰", previous_track_button: "⏮", prince: "🤴", princess: "👸", printer: "🖨", purple_heart: "💜", purse: "👛", pushpin: "📌", put_litter_in_its_place: "🚮", question: "❓", rabbit: "🐰", rabbit2: "🐇", racehorse: "🐎", racing_car: "🏎", radio: "📻", radio_button: "🔘", radioactive: "☢️", railway_car: "🚃", railway_track: "🛤", rainbow: "🌈", rainbow_flag: "🏳️&zwj;🌈", raised_back_of_hand: "🤚", raised_hand_with_fingers_splayed: "🖐", raised_hands: "🙌", raising_hand_woman: "🙋", raising_hand_man: "🙋&zwj;♂️", ram: "🐏", ramen: "🍜", rat: "🐀", record_button: "⏺", recycle: "♻️", red_circle: "🔴", registered: "®️", relaxed: "☺️", relieved: "😌", reminder_ribbon: "🎗", repeat: "🔁", repeat_one: "🔂", rescue_worker_helmet: "⛑", restroom: "🚻", revolving_hearts: "💞", rewind: "⏪", rhinoceros: "🦏", ribbon: "🎀", rice: "🍚", rice_ball: "🍙", rice_cracker: "🍘", rice_scene: "🎑", right_anger_bubble: "🗯", ring: "💍", robot: "🤖", rocket: "🚀", rofl: "🤣", roll_eyes: "🙄", roller_coaster: "🎢", rooster: "🐓", rose: "🌹", rosette: "🏵", rotating_light: "🚨", round_pushpin: "📍", rowing_man: "🚣", rowing_woman: "🚣&zwj;♀️", rugby_football: "🏉", running_man: "🏃", running_shirt_with_sash: "🎽", running_woman: "🏃&zwj;♀️", sa: "🈂️", sagittarius: "♐️", sake: "🍶", sandal: "👡", santa: "🎅", satellite: "📡", saxophone: "🎷", school: "🏫", school_satchel: "🎒", scissors: "✂️", scorpion: "🦂", scorpius: "♏️", scream: "😱", scream_cat: "🙀", scroll: "📜", seat: "💺", secret: "㊙️", see_no_evil: "🙈", seedling: "🌱", selfie: "🤳", shallow_pan_of_food: "🥘", shamrock: "☘️", shark: "🦈", shaved_ice: "🍧", sheep: "🐑", shell: "🐚", shield: "🛡", shinto_shrine: "⛩", ship: "🚢", shirt: "👕", shopping: "🛍", shopping_cart: "🛒", shower: "🚿", shrimp: "🦐", signal_strength: "📶", six_pointed_star: "🔯", ski: "🎿", skier: "⛷", skull: "💀", skull_and_crossbones: "☠️", sleeping: "😴", sleeping_bed: "🛌", sleepy: "😪", slightly_frowning_face: "🙁", slightly_smiling_face: "🙂", slot_machine: "🎰", small_airplane: "🛩", small_blue_diamond: "🔹", small_orange_diamond: "🔸", small_red_triangle: "🔺", small_red_triangle_down: "🔻", smile: "😄", smile_cat: "😸", smiley: "😃", smiley_cat: "😺", smiling_imp: "😈", smirk: "😏", smirk_cat: "😼", smoking: "🚬", snail: "🐌", snake: "🐍", sneezing_face: "🤧", snowboarder: "🏂", snowflake: "❄️", snowman: "⛄️", snowman_with_snow: "☃️", sob: "😭", soccer: "⚽️", soon: "🔜", sos: "🆘", sound: "🔉", space_invader: "👾", spades: "♠️", spaghetti: "🍝", sparkle: "❇️", sparkler: "🎇", sparkles: "✨", sparkling_heart: "💖", speak_no_evil: "🙊", speaker: "🔈", speaking_head: "🗣", speech_balloon: "💬", speedboat: "🚤", spider: "🕷", spider_web: "🕸", spiral_calendar: "🗓", spiral_notepad: "🗒", spoon: "🥄", squid: "🦑", stadium: "🏟", star: "⭐️", star2: "🌟", star_and_crescent: "☪️", star_of_david: "✡️", stars: "🌠", station: "🚉", statue_of_liberty: "🗽", steam_locomotive: "🚂", stew: "🍲", stop_button: "⏹", stop_sign: "🛑", stopwatch: "⏱", straight_ruler: "📏", strawberry: "🍓", stuck_out_tongue: "😛", stuck_out_tongue_closed_eyes: "😝", stuck_out_tongue_winking_eye: "😜", studio_microphone: "🎙", stuffed_flatbread: "🥙", sun_behind_large_cloud: "🌥", sun_behind_rain_cloud: "🌦", sun_behind_small_cloud: "🌤", sun_with_face: "🌞", sunflower: "🌻", sunglasses: "😎", sunny: "☀️", sunrise: "🌅", sunrise_over_mountains: "🌄", surfing_man: "🏄", surfing_woman: "🏄&zwj;♀️", sushi: "🍣", suspension_railway: "🚟", sweat: "😓", sweat_drops: "💦", sweat_smile: "😅", sweet_potato: "🍠", swimming_man: "🏊", swimming_woman: "🏊&zwj;♀️", symbols: "🔣", synagogue: "🕍", syringe: "💉", taco: "🌮", tada: "🎉", tanabata_tree: "🎋", taurus: "♉️", taxi: "🚕", tea: "🍵", telephone_receiver: "📞", telescope: "🔭", tennis: "🎾", tent: "⛺️", thermometer: "🌡", thinking: "🤔", thought_balloon: "💭", ticket: "🎫", tickets: "🎟", tiger: "🐯", tiger2: "🐅", timer_clock: "⏲", tipping_hand_man: "💁&zwj;♂️", tired_face: "😫", tm: "™️", toilet: "🚽", tokyo_tower: "🗼", tomato: "🍅", tongue: "👅", top: "🔝", tophat: "🎩", tornado: "🌪", trackball: "🖲", tractor: "🚜", traffic_light: "🚥", train: "🚋", train2: "🚆", tram: "🚊", triangular_flag_on_post: "🚩", triangular_ruler: "📐", trident: "🔱", triumph: "😤", trolleybus: "🚎", trophy: "🏆", tropical_drink: "🍹", tropical_fish: "🐠", truck: "🚚", trumpet: "🎺", tulip: "🌷", tumbler_glass: "🥃", turkey: "🦃", turtle: "🐢", tv: "📺", twisted_rightwards_arrows: "🔀", two_hearts: "💕", two_men_holding_hands: "👬", two_women_holding_hands: "👭", u5272: "🈹", u5408: "🈴", u55b6: "🈺", u6307: "🈯️", u6708: "🈷️", u6709: "🈶", u6e80: "🈵", u7121: "🈚️", u7533: "🈸", u7981: "🈲", u7a7a: "🈳", umbrella: "☔️", unamused: "😒", underage: "🔞", unicorn: "🦄", unlock: "🔓", up: "🆙", upside_down_face: "🙃", v: "✌️", vertical_traffic_light: "🚦", vhs: "📼", vibration_mode: "📳", video_camera: "📹", video_game: "🎮", violin: "🎻", virgo: "♍️", volcano: "🌋", volleyball: "🏐", vs: "🆚", vulcan_salute: "🖖", walking_man: "🚶", walking_woman: "🚶&zwj;♀️", waning_crescent_moon: "🌘", waning_gibbous_moon: "🌖", warning: "⚠️", wastebasket: "🗑", watch: "⌚️", water_buffalo: "🐃", watermelon: "🍉", wave: "👋", wavy_dash: "〰️", waxing_crescent_moon: "🌒", wc: "🚾", weary: "😩", wedding: "💒", weight_lifting_man: "🏋️", weight_lifting_woman: "🏋️&zwj;♀️", whale: "🐳", whale2: "🐋", wheel_of_dharma: "☸️", wheelchair: "♿️", white_check_mark: "✅", white_circle: "⚪️", white_flag: "🏳️", white_flower: "💮", white_large_square: "⬜️", white_medium_small_square: "◽️", white_medium_square: "◻️", white_small_square: "▫️", white_square_button: "🔳", wilted_flower: "🥀", wind_chime: "🎐", wind_face: "🌬", wine_glass: "🍷", wink: "😉", wolf: "🐺", woman: "👩", woman_artist: "👩&zwj;🎨", woman_astronaut: "👩&zwj;🚀", woman_cartwheeling: "🤸&zwj;♀️", woman_cook: "👩&zwj;🍳", woman_facepalming: "🤦&zwj;♀️", woman_factory_worker: "👩&zwj;🏭", woman_farmer: "👩&zwj;🌾", woman_firefighter: "👩&zwj;🚒", woman_health_worker: "👩&zwj;⚕️", woman_judge: "👩&zwj;⚖️", woman_juggling: "🤹&zwj;♀️", woman_mechanic: "👩&zwj;🔧", woman_office_worker: "👩&zwj;💼", woman_pilot: "👩&zwj;✈️", woman_playing_handball: "🤾&zwj;♀️", woman_playing_water_polo: "🤽&zwj;♀️", woman_scientist: "👩&zwj;🔬", woman_shrugging: "🤷&zwj;♀️", woman_singer: "👩&zwj;🎤", woman_student: "👩&zwj;🎓", woman_teacher: "👩&zwj;🏫", woman_technologist: "👩&zwj;💻", woman_with_turban: "👳&zwj;♀️", womans_clothes: "👚", womans_hat: "👒", women_wrestling: "🤼&zwj;♀️", womens: "🚺", world_map: "🗺", worried: "😟", wrench: "🔧", writing_hand: "✍️", x: "❌", yellow_heart: "💛", yen: "💴", yin_yang: "☯️", yum: "😋", zap: "⚡️", zipper_mouth_face: "🤐", zzz: "💤", octocat: '<img alt=":octocat:" height="20" width="20" align="absmiddle" src="https://assets-cdn.github.com/images/icons/emoji/octocat.png">', showdown: "<span style=\"font-family: 'Anonymous Pro', monospace; text-decoration: underline; text-decoration-style: dashed; text-decoration-color: #3e8b8a;text-underline-position: under;\">S</span>" }, a.Converter = function (e) { "use strict"; function t(e, t) { if (t = t || null, a.helper.isString(e)) { if (e = a.helper.stdExtName(e), t = e, a.extensions[e]) return console.warn("DEPRECATION WARNING: " + e + " is an old extension that uses a deprecated loading method.Please inform the developer that the extension should be updated!"), void function (e, t) { "function" == typeof e && (e = e(new a.Converter)); a.helper.isArray(e) || (e = [e]); var n = r(e, t); if (!n.valid) throw Error(n.error); for (var s = 0; s < e.length; ++s)switch (e[s].type) { case "lang": u.push(e[s]); break; case "output": d.push(e[s]); break; default: throw Error("Extension loader error: Type unrecognized!!!") } }(a.extensions[e], e); if (a.helper.isUndefined(s[e])) throw Error('Extension "' + e + '" could not be loaded. It was either not found or is not a valid extension.'); e = s[e] } "function" == typeof e && (e = e()), a.helper.isArray(e) || (e = [e]); var o = r(e, t); if (!o.valid) throw Error(o.error); for (var i = 0; i < e.length; ++i) { switch (e[i].type) { case "lang": u.push(e[i]); break; case "output": d.push(e[i]) }if (e[i].hasOwnProperty("listeners")) for (var l in e[i].listeners) e[i].listeners.hasOwnProperty(l) && n(l, e[i].listeners[l]) } } function n(e, r) { if (!a.helper.isString(e)) throw Error("Invalid argument in converter.listen() method: name must be a string, but " + typeof e + " given"); if ("function" != typeof r) throw Error("Invalid argument in converter.listen() method: callback must be a function, but " + typeof r + " given"); p.hasOwnProperty(e) || (p[e] = []), p[e].push(r) } var c = {}, u = [], d = [], p = {}, h = i, _ = { parsed: {}, raw: "", format: "" }; !function () { e = e || {}; for (var r in o) o.hasOwnProperty(r) && (c[r] = o[r]); if ("object" != typeof e) throw Error("Converter expects the passed parameter to be an object, but " + typeof e + " was passed instead."); for (var n in e) e.hasOwnProperty(n) && (c[n] = e[n]); c.extensions && a.helper.forEach(c.extensions, t) }(), this._dispatch = function (e, r, t, a) { if (p.hasOwnProperty(e)) for (var n = 0; n < p[e].length; ++n) { var s = p[e][n](e, r, this, t, a); s && void 0 !== s && (r = s) } return r }, this.listen = function (e, r) { return n(e, r), this }, this.makeHtml = function (e) { if (!e) return e; var r = { gHtmlBlocks: [], gHtmlMdBlocks: [], gHtmlSpans: [], gUrls: {}, gTitles: {}, gDimensions: {}, gListLevel: 0, hashLinkCounts: {}, langExtensions: u, outputModifiers: d, converter: this, ghCodeBlocks: [], metadata: { parsed: {}, raw: "", format: "" } }; return e = e.replace(/¨/g, "¨T"), e = e.replace(/\$/g, "¨D"), e = e.replace(/\r\n/g, "\n"), e = e.replace(/\r/g, "\n"), e = e.replace(/\u00A0/g, "&nbsp;"), c.smartIndentationFix && (e = function (e) { var r = e.match(/^\s*/)[0].length, t = new RegExp("^\\s{0," + r + "}", "gm"); return e.replace(t, "") }(e)), e = "\n\n" + e + "\n\n", e = a.subParser("detab")(e, c, r), e = e.replace(/^[ \t]+$/gm, ""), a.helper.forEach(u, function (t) { e = a.subParser("runExtension")(t, e, c, r) }), e = a.subParser("metadata")(e, c, r), e = a.subParser("hashPreCodeTags")(e, c, r), e = a.subParser("githubCodeBlocks")(e, c, r), e = a.subParser("hashHTMLBlocks")(e, c, r), e = a.subParser("hashCodeTags")(e, c, r), e = a.subParser("stripLinkDefinitions")(e, c, r), e = a.subParser("blockGamut")(e, c, r), e = a.subParser("unhashHTMLSpans")(e, c, r), e = a.subParser("unescapeSpecialChars")(e, c, r), e = e.replace(/¨D/g, "$$"), e = e.replace(/¨T/g, "¨"), e = a.subParser("completeHTMLDocument")(e, c, r), a.helper.forEach(d, function (t) { e = a.subParser("runExtension")(t, e, c, r) }), _ = r.metadata, e }, this.makeMarkdown = this.makeMd = function (e, r) { function t(e) { for (var r = 0; r < e.childNodes.length; ++r) { var a = e.childNodes[r]; 3 === a.nodeType ? /\S/.test(a.nodeValue) ? (a.nodeValue = a.nodeValue.split("\n").join(" "), a.nodeValue = a.nodeValue.replace(/(\s)+/g, "$1")) : (e.removeChild(a), --r) : 1 === a.nodeType && t(a) } } if (e = e.replace(/\r\n/g, "\n"), e = e.replace(/\r/g, "\n"), e = e.replace(/>[ \t]+</, ">¨NBSP;<"), !r) { if (!window || !window.document) throw new Error("HTMLParser is undefined. If in a webworker or nodejs environment, you need to provide a WHATWG DOM and HTML such as JSDOM"); r = window.document } var n = r.createElement("div"); n.innerHTML = e; var s = { preList: function (e) { for (var r = e.querySelectorAll("pre"), t = [], n = 0; n < r.length; ++n)if (1 === r[n].childElementCount && "code" === r[n].firstChild.tagName.toLowerCase()) { var s = r[n].firstChild.innerHTML.trim(), o = r[n].firstChild.getAttribute("data-language") || ""; if ("" === o) for (var i = r[n].firstChild.className.split(" "), l = 0; l < i.length; ++l) { var c = i[l].match(/^language-(.+)$/); if (null !== c) { o = c[1]; break } } s = a.helper.unescapeHTMLEntities(s), t.push(s), r[n].outerHTML = '<precode language="' + o + '" precodenum="' + n.toString() + '"></precode>' } else t.push(r[n].innerHTML), r[n].innerHTML = "", r[n].setAttribute("prenum", n.toString()); return t }(n) }; t(n); for (var o = n.childNodes, i = "", l = 0; l < o.length; l++)i += a.subParser("makeMarkdown.node")(o[l], s); return i }, this.setOption = function (e, r) { c[e] = r }, this.getOption = function (e) { return c[e] }, this.getOptions = function () { return c }, this.addExtension = function (e, r) { t(e, r = r || null) }, this.useExtension = function (e) { t(e) }, this.setFlavor = function (e) { if (!l.hasOwnProperty(e)) throw Error(e + " flavor was not found"); var r = l[e]; h = e; for (var t in r) r.hasOwnProperty(t) && (c[t] = r[t]) }, this.getFlavor = function () { return h }, this.removeExtension = function (e) { a.helper.isArray(e) || (e = [e]); for (var r = 0; r < e.length; ++r) { for (var t = e[r], n = 0; n < u.length; ++n)u[n] === t && u[n].splice(n, 1); for (; 0 < d.length; ++n)d[0] === t && d[0].splice(n, 1) } }, this.getAllExtensions = function () { return { language: u, output: d } }, this.getMetadata = function (e) { return e ? _.raw : _.parsed }, this.getMetadataFormat = function () { return _.format }, this._setMetadataPair = function (e, r) { _.parsed[e] = r }, this._setMetadataFormat = function (e) { _.format = e }, this._setMetadataRaw = function (e) { _.raw = e } }, a.subParser("anchors", function (e, r, t) { "use strict"; var n = function (e, n, s, o, i, l, c) { if (a.helper.isUndefined(c) && (c = ""), s = s.toLowerCase(), e.search(/\(<?\s*>? ?(['"].*['"])?\)$/m) > -1) o = ""; else if (!o) { if (s || (s = n.toLowerCase().replace(/ ?\n/g, " ")), o = "#" + s, a.helper.isUndefined(t.gUrls[s])) return e; o = t.gUrls[s], a.helper.isUndefined(t.gTitles[s]) || (c = t.gTitles[s]) } var u = '<a href="' + (o = o.replace(a.helper.regexes.asteriskDashAndColon, a.helper.escapeCharactersCallback)) + '"'; return "" !== c && null !== c && (u += ' title="' + (c = (c = c.replace(/"/g, "&quot;")).replace(a.helper.regexes.asteriskDashAndColon, a.helper.escapeCharactersCallback)) + '"'), r.openLinksInNewWindow && !/^#/.test(o) && (u += ' rel="noopener noreferrer" target="¨E95Eblank"'), u += ">" + n + "</a>" }; return e = (e = t.converter._dispatch("anchors.before", e, r, t)).replace(/\[((?:\[[^\]]*]|[^\[\]])*)] ?(?:\n *)?\[(.*?)]()()()()/g, n), e = e.replace(/\[((?:\[[^\]]*]|[^\[\]])*)]()[ \t]*\([ \t]?<([^>]*)>(?:[ \t]*((["'])([^"]*?)\5))?[ \t]?\)/g, n), e = e.replace(/\[((?:\[[^\]]*]|[^\[\]])*)]()[ \t]*\([ \t]?<?([\S]+?(?:\([\S]*?\)[\S]*?)?)>?(?:[ \t]*((["'])([^"]*?)\5))?[ \t]?\)/g, n), e = e.replace(/\[([^\[\]]+)]()()()()()/g, n), r.ghMentions && (e = e.replace(/(^|\s)(\\)?(@([a-z\d]+(?:[a-z\d.-]+?[a-z\d]+)*))/gim, function (e, t, n, s, o) { if ("\\" === n) return t + s; if (!a.helper.isString(r.ghMentionsLink)) throw new Error("ghMentionsLink option must be a string"); var i = r.ghMentionsLink.replace(/\{u}/g, o), l = ""; return r.openLinksInNewWindow && (l = ' rel="noopener noreferrer" target="¨E95Eblank"'), t + '<a href="' + i + '"' + l + ">" + s + "</a>" })), e = t.converter._dispatch("anchors.after", e, r, t) }); var u = /([*~_]+|\b)(((https?|ftp|dict):\/\/|www\.)[^'">\s]+?\.[^'">\s]+?)()(\1)?(?=\s|$)(?!["<>])/gi, d = /([*~_]+|\b)(((https?|ftp|dict):\/\/|www\.)[^'">\s]+\.[^'">\s]+?)([.!?,()\[\]])?(\1)?(?=\s|$)(?!["<>])/gi, p = /()<(((https?|ftp|dict):\/\/|www\.)[^'">\s]+)()>()/gi, h = /(^|\s)(?:mailto:)?([A-Za-z0-9!#$%&'*+-/=?^_`{|}~.]+@[-a-z0-9]+(\.[-a-z0-9]+)*\.[a-z]+)(?=$|\s)/gim, _ = /<()(?:mailto:)?([-.\w]+@[-a-z0-9]+(\.[-a-z0-9]+)*\.[a-z]+)>/gi, g = function (e) { "use strict"; return function (r, t, n, s, o, i, l) { var c = n = n.replace(a.helper.regexes.asteriskDashAndColon, a.helper.escapeCharactersCallback), u = "", d = "", p = t || "", h = l || ""; return /^www\./i.test(n) && (n = n.replace(/^www\./i, "http://www.")), e.excludeTrailingPunctuationFromURLs && i && (u = i), e.openLinksInNewWindow && (d = ' rel="noopener noreferrer" target="¨E95Eblank"'), p + '<a href="' + n + '"' + d + ">" + c + "</a>" + u + h } }, m = function (e, r) { "use strict"; return function (t, n, s) { var o = "mailto:"; return n = n || "", s = a.subParser("unescapeSpecialChars")(s, e, r), e.encodeEmails ? (o = a.helper.encodeEmailAddress(o + s), s = a.helper.encodeEmailAddress(s)) : o += s, n + '<a href="' + o + '">' + s + "</a>" } }; a.subParser("autoLinks", function (e, r, t) { "use strict"; return e = t.converter._dispatch("autoLinks.before", e, r, t), e = e.replace(p, g(r)), e = e.replace(_, m(r, t)), e = t.converter._dispatch("autoLinks.after", e, r, t) }), a.subParser("simplifiedAutoLinks", function (e, r, t) { "use strict"; return r.simplifiedAutoLink ? (e = t.converter._dispatch("simplifiedAutoLinks.before", e, r, t), e = r.excludeTrailingPunctuationFromURLs ? e.replace(d, g(r)) : e.replace(u, g(r)), e = e.replace(h, m(r, t)), e = t.converter._dispatch("simplifiedAutoLinks.after", e, r, t)) : e }), a.subParser("blockGamut", function (e, r, t) { "use strict"; return e = t.converter._dispatch("blockGamut.before", e, r, t), e = a.subParser("blockQuotes")(e, r, t), e = a.subParser("headers")(e, r, t), e = a.subParser("horizontalRule")(e, r, t), e = a.subParser("lists")(e, r, t), e = a.subParser("codeBlocks")(e, r, t), e = a.subParser("tables")(e, r, t), e = a.subParser("hashHTMLBlocks")(e, r, t), e = a.subParser("paragraphs")(e, r, t), e = t.converter._dispatch("blockGamut.after", e, r, t) }), a.subParser("blockQuotes", function (e, r, t) { "use strict"; e = t.converter._dispatch("blockQuotes.before", e, r, t), e += "\n\n"; var n = /(^ {0,3}>[ \t]?.+\n(.+\n)*\n*)+/gm; return r.splitAdjacentBlockquotes && (n = /^ {0,3}>[\s\S]*?(?:\n\n)/gm), e = e.replace(n, function (e) { return e = e.replace(/^[ \t]*>[ \t]?/gm, ""), e = e.replace(/¨0/g, ""), e = e.replace(/^[ \t]+$/gm, ""), e = a.subParser("githubCodeBlocks")(e, r, t), e = a.subParser("blockGamut")(e, r, t), e = e.replace(/(^|\n)/g, "$1  "), e = e.replace(/(\s*<pre>[^\r]+?<\/pre>)/gm, function (e, r) { var t = r; return t = t.replace(/^  /gm, "¨0"), t = t.replace(/¨0/g, "") }), a.subParser("hashBlock")("<blockquote>\n" + e + "\n</blockquote>", r, t) }), e = t.converter._dispatch("blockQuotes.after", e, r, t) }), a.subParser("codeBlocks", function (e, r, t) { "use strict"; e = t.converter._dispatch("codeBlocks.before", e, r, t); return e = (e += "¨0").replace(/(?:\n\n|^)((?:(?:[ ]{4}|\t).*\n+)+)(\n*[ ]{0,3}[^ \t\n]|(?=¨0))/g, function (e, n, s) { var o = n, i = s, l = "\n"; return o = a.subParser("outdent")(o, r, t), o = a.subParser("encodeCode")(o, r, t), o = a.subParser("detab")(o, r, t), o = o.replace(/^\n+/g, ""), o = o.replace(/\n+$/g, ""), r.omitExtraWLInCodeBlocks && (l = ""), o = "<pre><code>" + o + l + "</code></pre>", a.subParser("hashBlock")(o, r, t) + i }), e = e.replace(/¨0/, ""), e = t.converter._dispatch("codeBlocks.after", e, r, t) }), a.subParser("codeSpans", function (e, r, t) { "use strict"; return void 0 === (e = t.converter._dispatch("codeSpans.before", e, r, t)) && (e = ""), e = e.replace(/(^|[^\\])(`+)([^\r]*?[^`])\2(?!`)/gm, function (e, n, s, o) { var i = o; return i = i.replace(/^([ \t]*)/g, ""), i = i.replace(/[ \t]*$/g, ""), i = a.subParser("encodeCode")(i, r, t), i = n + "<code>" + i + "</code>", i = a.subParser("hashHTMLSpans")(i, r, t) }), e = t.converter._dispatch("codeSpans.after", e, r, t) }), a.subParser("completeHTMLDocument", function (e, r, t) { "use strict"; if (!r.completeHTMLDocument) return e; e = t.converter._dispatch("completeHTMLDocument.before", e, r, t); var a = "html", n = "<!DOCTYPE HTML>\n", s = "", o = '<meta charset="utf-8">\n', i = "", l = ""; void 0 !== t.metadata.parsed.doctype && (n = "<!DOCTYPE " + t.metadata.parsed.doctype + ">\n", "html" !== (a = t.metadata.parsed.doctype.toString().toLowerCase()) && "html5" !== a || (o = '<meta charset="utf-8">')); for (var c in t.metadata.parsed) if (t.metadata.parsed.hasOwnProperty(c)) switch (c.toLowerCase()) { case "doctype": break; case "title": s = "<title>" + t.metadata.parsed.title + "</title>\n"; break; case "charset": o = "html" === a || "html5" === a ? '<meta charset="' + t.metadata.parsed.charset + '">\n' : '<meta name="charset" content="' + t.metadata.parsed.charset + '">\n'; break; case "language": case "lang": i = ' lang="' + t.metadata.parsed[c] + '"', l += '<meta name="' + c + '" content="' + t.metadata.parsed[c] + '">\n'; break; default: l += '<meta name="' + c + '" content="' + t.metadata.parsed[c] + '">\n' }return e = n + "<html" + i + ">\n<head>\n" + s + o + l + "</head>\n<body>\n" + e.trim() + "\n</body>\n</html>", e = t.converter._dispatch("completeHTMLDocument.after", e, r, t) }), a.subParser("detab", function (e, r, t) { "use strict"; return e = t.converter._dispatch("detab.before", e, r, t), e = e.replace(/\t(?=\t)/g, "    "), e = e.replace(/\t/g, "¨A¨B"), e = e.replace(/¨B(.+?)¨A/g, function (e, r) { for (var t = r, a = 4 - t.length % 4, n = 0; n < a; n++)t += " "; return t }), e = e.replace(/¨A/g, "    "), e = e.replace(/¨B/g, ""), e = t.converter._dispatch("detab.after", e, r, t) }), a.subParser("ellipsis", function (e, r, t) { "use strict"; return e = t.converter._dispatch("ellipsis.before", e, r, t), e = e.replace(/\.\.\./g, "…"), e = t.converter._dispatch("ellipsis.after", e, r, t) }), a.subParser("emoji", function (e, r, t) { "use strict"; if (!r.emoji) return e; return e = (e = t.converter._dispatch("emoji.before", e, r, t)).replace(/:([\S]+?):/g, function (e, r) { return a.helper.emojis.hasOwnProperty(r) ? a.helper.emojis[r] : e }), e = t.converter._dispatch("emoji.after", e, r, t) }), a.subParser("encodeAmpsAndAngles", function (e, r, t) { "use strict"; return e = t.converter._dispatch("encodeAmpsAndAngles.before", e, r, t), e = e.replace(/&(?!#?[xX]?(?:[0-9a-fA-F]+|\w+);)/g, "&amp;"), e = e.replace(/<(?![a-z\/?$!])/gi, "&lt;"), e = e.replace(/</g, "&lt;"), e = e.replace(/>/g, "&gt;"), e = t.converter._dispatch("encodeAmpsAndAngles.after", e, r, t) }), a.subParser("encodeBackslashEscapes", function (e, r, t) { "use strict"; return e = t.converter._dispatch("encodeBackslashEscapes.before", e, r, t), e = e.replace(/\\(\\)/g, a.helper.escapeCharactersCallback), e = e.replace(/\\([`*_{}\[\]()>#+.!~=|-])/g, a.helper.escapeCharactersCallback), e = t.converter._dispatch("encodeBackslashEscapes.after", e, r, t) }), a.subParser("encodeCode", function (e, r, t) { "use strict"; return e = t.converter._dispatch("encodeCode.before", e, r, t), e = e.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/([*_{}\[\]\\=~-])/g, a.helper.escapeCharactersCallback), e = t.converter._dispatch("encodeCode.after", e, r, t) }), a.subParser("escapeSpecialCharsWithinTagAttributes", function (e, r, t) { "use strict"; return e = (e = t.converter._dispatch("escapeSpecialCharsWithinTagAttributes.before", e, r, t)).replace(/<\/?[a-z\d_:-]+(?:[\s]+[\s\S]+?)?>/gi, function (e) { return e.replace(/(.)<\/?code>(?=.)/g, "$1`").replace(/([\\`*_~=|])/g, a.helper.escapeCharactersCallback) }), e = e.replace(/<!(--(?:(?:[^>-]|-[^>])(?:[^-]|-[^-])*)--)>/gi, function (e) { return e.replace(/([\\`*_~=|])/g, a.helper.escapeCharactersCallback) }), e = t.converter._dispatch("escapeSpecialCharsWithinTagAttributes.after", e, r, t) }), a.subParser("githubCodeBlocks", function (e, r, t) { "use strict"; return r.ghCodeBlocks ? (e = t.converter._dispatch("githubCodeBlocks.before", e, r, t), e += "¨0", e = e.replace(/(?:^|\n)(?: {0,3})(```+|~~~+)(?: *)([^\s`~]*)\n([\s\S]*?)\n(?: {0,3})\1/g, function (e, n, s, o) { var i = r.omitExtraWLInCodeBlocks ? "" : "\n"; return o = a.subParser("encodeCode")(o, r, t), o = a.subParser("detab")(o, r, t), o = o.replace(/^\n+/g, ""), o = o.replace(/\n+$/g, ""), o = "<pre><code" + (s ? ' class="' + s + " language-" + s + '"' : "") + ">" + o + i + "</code></pre>", o = a.subParser("hashBlock")(o, r, t), "\n\n¨G" + (t.ghCodeBlocks.push({ text: e, codeblock: o }) - 1) + "G\n\n" }), e = e.replace(/¨0/, ""), t.converter._dispatch("githubCodeBlocks.after", e, r, t)) : e }), a.subParser("hashBlock", function (e, r, t) { "use strict"; return e = t.converter._dispatch("hashBlock.before", e, r, t), e = e.replace(/(^\n+|\n+$)/g, ""), e = "\n\n¨K" + (t.gHtmlBlocks.push(e) - 1) + "K\n\n", e = t.converter._dispatch("hashBlock.after", e, r, t) }), a.subParser("hashCodeTags", function (e, r, t) { "use strict"; e = t.converter._dispatch("hashCodeTags.before", e, r, t); return e = a.helper.replaceRecursiveRegExp(e, function (e, n, s, o) { var i = s + a.subParser("encodeCode")(n, r, t) + o; return "¨C" + (t.gHtmlSpans.push(i) - 1) + "C" }, "<code\\b[^>]*>", "</code>", "gim"), e = t.converter._dispatch("hashCodeTags.after", e, r, t) }), a.subParser("hashElement", function (e, r, t) { "use strict"; return function (e, r) { var a = r; return a = a.replace(/\n\n/g, "\n"), a = a.replace(/^\n/, ""), a = a.replace(/\n+$/g, ""), a = "\n\n¨K" + (t.gHtmlBlocks.push(a) - 1) + "K\n\n" } }), a.subParser("hashHTMLBlocks", function (e, r, t) { "use strict"; e = t.converter._dispatch("hashHTMLBlocks.before", e, r, t); var n = ["pre", "div", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "table", "dl", "ol", "ul", "script", "noscript", "form", "fieldset", "iframe", "math", "style", "section", "header", "footer", "nav", "article", "aside", "address", "audio", "canvas", "figure", "hgroup", "output", "video", "p"], s = function (e, r, a, n) { var s = e; return -1 !== a.search(/\bmarkdown\b/) && (s = a + t.converter.makeHtml(r) + n), "\n\n¨K" + (t.gHtmlBlocks.push(s) - 1) + "K\n\n" }; r.backslashEscapesHTMLTags && (e = e.replace(/\\<(\/?[^>]+?)>/g, function (e, r) { return "&lt;" + r + "&gt;" })); for (var o = 0; o < n.length; ++o)for (var i, l = new RegExp("^ {0,3}(<" + n[o] + "\\b[^>]*>)", "im"), c = "<" + n[o] + "\\b[^>]*>", u = "</" + n[o] + ">"; -1 !== (i = a.helper.regexIndexOf(e, l));) { var d = a.helper.splitAtIndex(e, i), p = a.helper.replaceRecursiveRegExp(d[1], s, c, u, "im"); if (p === d[1]) break; e = d[0].concat(p) } return e = e.replace(/(\n {0,3}(<(hr)\b([^<>])*?\/?>)[ \t]*(?=\n{2,}))/g, a.subParser("hashElement")(e, r, t)), e = a.helper.replaceRecursiveRegExp(e, function (e) { return "\n\n¨K" + (t.gHtmlBlocks.push(e) - 1) + "K\n\n" }, "^ {0,3}\x3c!--", "--\x3e", "gm"), e = e.replace(/(?:\n\n)( {0,3}(?:<([?%])[^\r]*?\2>)[ \t]*(?=\n{2,}))/g, a.subParser("hashElement")(e, r, t)), e = t.converter._dispatch("hashHTMLBlocks.after", e, r, t) }), a.subParser("hashHTMLSpans", function (e, r, t) { "use strict"; function a(e) { return "¨C" + (t.gHtmlSpans.push(e) - 1) + "C" } return e = t.converter._dispatch("hashHTMLSpans.before", e, r, t), e = e.replace(/<[^>]+?\/>/gi, function (e) { return a(e) }), e = e.replace(/<([^>]+?)>[\s\S]*?<\/\1>/g, function (e) { return a(e) }), e = e.replace(/<([^>]+?)\s[^>]+?>[\s\S]*?<\/\1>/g, function (e) { return a(e) }), e = e.replace(/<[^>]+?>/gi, function (e) { return a(e) }), e = t.converter._dispatch("hashHTMLSpans.after", e, r, t) }), a.subParser("unhashHTMLSpans", function (e, r, t) { "use strict"; e = t.converter._dispatch("unhashHTMLSpans.before", e, r, t); for (var a = 0; a < t.gHtmlSpans.length; ++a) { for (var n = t.gHtmlSpans[a], s = 0; /¨C(\d+)C/.test(n);) { var o = RegExp.$1; if (n = n.replace("¨C" + o + "C", t.gHtmlSpans[o]), 10 === s) { console.error("maximum nesting of 10 spans reached!!!"); break } ++s } e = e.replace("¨C" + a + "C", n) } return e = t.converter._dispatch("unhashHTMLSpans.after", e, r, t) }), a.subParser("hashPreCodeTags", function (e, r, t) { "use strict"; e = t.converter._dispatch("hashPreCodeTags.before", e, r, t); return e = a.helper.replaceRecursiveRegExp(e, function (e, n, s, o) { var i = s + a.subParser("encodeCode")(n, r, t) + o; return "\n\n¨G" + (t.ghCodeBlocks.push({ text: e, codeblock: i }) - 1) + "G\n\n" }, "^ {0,3}<pre\\b[^>]*>\\s*<code\\b[^>]*>", "^ {0,3}</code>\\s*</pre>", "gim"), e = t.converter._dispatch("hashPreCodeTags.after", e, r, t) }), a.subParser("headers", function (e, r, t) { "use strict"; function n(e) { var n, s; if (r.customizedHeaderId) { var o = e.match(/\{([^{]+?)}\s*$/); o && o[1] && (e = o[1]) } return n = e, s = a.helper.isString(r.prefixHeaderId) ? r.prefixHeaderId : !0 === r.prefixHeaderId ? "section-" : "", r.rawPrefixHeaderId || (n = s + n), n = r.ghCompatibleHeaderId ? n.replace(/ /g, "-").replace(/&amp;/g, "").replace(/¨T/g, "").replace(/¨D/g, "").replace(/[&+$,\/:;=?@"#{}|^¨~\[\]`\\*)(%.!'<>]/g, "").toLowerCase() : r.rawHeaderId ? n.replace(/ /g, "-").replace(/&amp;/g, "&").replace(/¨T/g, "¨").replace(/¨D/g, "$").replace(/["']/g, "-").toLowerCase() : n.replace(/[^\w]/g, "").toLowerCase(), r.rawPrefixHeaderId && (n = s + n), t.hashLinkCounts[n] ? n = n + "-" + t.hashLinkCounts[n]++ : t.hashLinkCounts[n] = 1, n } e = t.converter._dispatch("headers.before", e, r, t); var s = isNaN(parseInt(r.headerLevelStart)) ? 1 : parseInt(r.headerLevelStart), o = r.smoothLivePreview ? /^(.+)[ \t]*\n={2,}[ \t]*\n+/gm : /^(.+)[ \t]*\n=+[ \t]*\n+/gm, i = r.smoothLivePreview ? /^(.+)[ \t]*\n-{2,}[ \t]*\n+/gm : /^(.+)[ \t]*\n-+[ \t]*\n+/gm; e = (e = e.replace(o, function (e, o) { var i = a.subParser("spanGamut")(o, r, t), l = r.noHeaderId ? "" : ' id="' + n(o) + '"', c = "<h" + s + l + ">" + i + "</h" + s + ">"; return a.subParser("hashBlock")(c, r, t) })).replace(i, function (e, o) { var i = a.subParser("spanGamut")(o, r, t), l = r.noHeaderId ? "" : ' id="' + n(o) + '"', c = s + 1, u = "<h" + c + l + ">" + i + "</h" + c + ">"; return a.subParser("hashBlock")(u, r, t) }); var l = r.requireSpaceBeforeHeadingText ? /^(#{1,6})[ \t]+(.+?)[ \t]*#*\n+/gm : /^(#{1,6})[ \t]*(.+?)[ \t]*#*\n+/gm; return e = e.replace(l, function (e, o, i) { var l = i; r.customizedHeaderId && (l = i.replace(/\s?\{([^{]+?)}\s*$/, "")); var c = a.subParser("spanGamut")(l, r, t), u = r.noHeaderId ? "" : ' id="' + n(i) + '"', d = s - 1 + o.length, p = "<h" + d + u + ">" + c + "</h" + d + ">"; return a.subParser("hashBlock")(p, r, t) }), e = t.converter._dispatch("headers.after", e, r, t) }), a.subParser("horizontalRule", function (e, r, t) { "use strict"; e = t.converter._dispatch("horizontalRule.before", e, r, t); var n = a.subParser("hashBlock")("<hr />", r, t); return e = e.replace(/^ {0,2}( ?-){3,}[ \t]*$/gm, n), e = e.replace(/^ {0,2}( ?\*){3,}[ \t]*$/gm, n), e = e.replace(/^ {0,2}( ?_){3,}[ \t]*$/gm, n), e = t.converter._dispatch("horizontalRule.after", e, r, t) }), a.subParser("images", function (e, r, t) { "use strict"; function n(e, r, n, s, o, i, l, c) { var u = t.gUrls, d = t.gTitles, p = t.gDimensions; if (n = n.toLowerCase(), c || (c = ""), e.search(/\(<?\s*>? ?(['"].*['"])?\)$/m) > -1) s = ""; else if ("" === s || null === s) { if ("" !== n && null !== n || (n = r.toLowerCase().replace(/ ?\n/g, " ")), s = "#" + n, a.helper.isUndefined(u[n])) return e; s = u[n], a.helper.isUndefined(d[n]) || (c = d[n]), a.helper.isUndefined(p[n]) || (o = p[n].width, i = p[n].height) } r = r.replace(/"/g, "&quot;").replace(a.helper.regexes.asteriskDashAndColon, a.helper.escapeCharactersCallback); var h = '<img src="' + (s = s.replace(a.helper.regexes.asteriskDashAndColon, a.helper.escapeCharactersCallback)) + '" alt="' + r + '"'; return c && a.helper.isString(c) && (h += ' title="' + (c = c.replace(/"/g, "&quot;").replace(a.helper.regexes.asteriskDashAndColon, a.helper.escapeCharactersCallback)) + '"'), o && i && (h += ' width="' + (o = "*" === o ? "auto" : o) + '"', h += ' height="' + (i = "*" === i ? "auto" : i) + '"'), h += " />" } return e = (e = t.converter._dispatch("images.before", e, r, t)).replace(/!\[([^\]]*?)] ?(?:\n *)?\[([\s\S]*?)]()()()()()/g, n), e = e.replace(/!\[([^\]]*?)][ \t]*()\([ \t]?<?(data:.+?\/.+?;base64,[A-Za-z0-9+/=\n]+?)>?(?: =([*\d]+[A-Za-z%]{0,4})x([*\d]+[A-Za-z%]{0,4}))?[ \t]*(?:(["'])([^"]*?)\6)?[ \t]?\)/g, function (e, r, t, a, s, o, i, l) { return a = a.replace(/\s/g, ""), n(e, r, t, a, s, o, 0, l) }), e = e.replace(/!\[([^\]]*?)][ \t]*()\([ \t]?<([^>]*)>(?: =([*\d]+[A-Za-z%]{0,4})x([*\d]+[A-Za-z%]{0,4}))?[ \t]*(?:(?:(["'])([^"]*?)\6))?[ \t]?\)/g, n), e = e.replace(/!\[([^\]]*?)][ \t]*()\([ \t]?<?([\S]+?(?:\([\S]*?\)[\S]*?)?)>?(?: =([*\d]+[A-Za-z%]{0,4})x([*\d]+[A-Za-z%]{0,4}))?[ \t]*(?:(["'])([^"]*?)\6)?[ \t]?\)/g, n), e = e.replace(/!\[([^\[\]]+)]()()()()()/g, n), e = t.converter._dispatch("images.after", e, r, t) }), a.subParser("italicsAndBold", function (e, r, t) { "use strict"; function a(e, r, t) { return r + e + t } return e = t.converter._dispatch("italicsAndBold.before", e, r, t), e = r.literalMidWordUnderscores ? (e = (e = e.replace(/\b___(\S[\s\S]*?)___\b/g, function (e, r) { return a(r, "<strong><em>", "</em></strong>") })).replace(/\b__(\S[\s\S]*?)__\b/g, function (e, r) { return a(r, "<strong>", "</strong>") })).replace(/\b_(\S[\s\S]*?)_\b/g, function (e, r) { return a(r, "<em>", "</em>") }) : (e = (e = e.replace(/___(\S[\s\S]*?)___/g, function (e, r) { return /\S$/.test(r) ? a(r, "<strong><em>", "</em></strong>") : e })).replace(/__(\S[\s\S]*?)__/g, function (e, r) { return /\S$/.test(r) ? a(r, "<strong>", "</strong>") : e })).replace(/_([^\s_][\s\S]*?)_/g, function (e, r) { return /\S$/.test(r) ? a(r, "<em>", "</em>") : e }), e = r.literalMidWordAsterisks ? (e = (e = e.replace(/([^*]|^)\B\*\*\*(\S[\s\S]*?)\*\*\*\B(?!\*)/g, function (e, r, t) { return a(t, r + "<strong><em>", "</em></strong>") })).replace(/([^*]|^)\B\*\*(\S[\s\S]*?)\*\*\B(?!\*)/g, function (e, r, t) { return a(t, r + "<strong>", "</strong>") })).replace(/([^*]|^)\B\*(\S[\s\S]*?)\*\B(?!\*)/g, function (e, r, t) { return a(t, r + "<em>", "</em>") }) : (e = (e = e.replace(/\*\*\*(\S[\s\S]*?)\*\*\*/g, function (e, r) { return /\S$/.test(r) ? a(r, "<strong><em>", "</em></strong>") : e })).replace(/\*\*(\S[\s\S]*?)\*\*/g, function (e, r) { return /\S$/.test(r) ? a(r, "<strong>", "</strong>") : e })).replace(/\*([^\s*][\s\S]*?)\*/g, function (e, r) { return /\S$/.test(r) ? a(r, "<em>", "</em>") : e }), e = t.converter._dispatch("italicsAndBold.after", e, r, t) }), a.subParser("lists", function (e, r, t) { "use strict"; function n(e, n) { t.gListLevel++, e = e.replace(/\n{2,}$/, "\n"); var s = /(\n)?(^ {0,3})([*+-]|\d+[.])[ \t]+((\[(x|X| )?])?[ \t]*[^\r]+?(\n{1,2}))(?=\n*(¨0| {0,3}([*+-]|\d+[.])[ \t]+))/gm, o = /\n[ \t]*\n(?!¨0)/.test(e += "¨0"); return r.disableForced4SpacesIndentedSublists && (s = /(\n)?(^ {0,3})([*+-]|\d+[.])[ \t]+((\[(x|X| )?])?[ \t]*[^\r]+?(\n{1,2}))(?=\n*(¨0|\2([*+-]|\d+[.])[ \t]+))/gm), e = e.replace(s, function (e, n, s, i, l, c, u) { u = u && "" !== u.trim(); var d = a.subParser("outdent")(l, r, t), p = ""; return c && r.tasklists && (p = ' class="task-list-item" style="list-style-type: none;"', d = d.replace(/^[ \t]*\[(x|X| )?]/m, function () { var e = '<input type="checkbox" disabled style="margin: 0px 0.35em 0.25em -1.6em; vertical-align: middle;"'; return u && (e += " checked"), e += ">" })), d = d.replace(/^([-*+]|\d\.)[ \t]+[\S\n ]*/g, function (e) { return "¨A" + e }), n || d.search(/\n{2,}/) > -1 ? (d = a.subParser("githubCodeBlocks")(d, r, t), d = a.subParser("blockGamut")(d, r, t)) : (d = (d = a.subParser("lists")(d, r, t)).replace(/\n$/, ""), d = (d = a.subParser("hashHTMLBlocks")(d, r, t)).replace(/\n\n+/g, "\n\n"), d = o ? a.subParser("paragraphs")(d, r, t) : a.subParser("spanGamut")(d, r, t)), d = d.replace("¨A", ""), d = "<li" + p + ">" + d + "</li>\n" }), e = e.replace(/¨0/g, ""), t.gListLevel--, n && (e = e.replace(/\s+$/, "")), e } function s(e, r) { if ("ol" === r) { var t = e.match(/^ *(\d+)\./); if (t && "1" !== t[1]) return ' start="' + t[1] + '"' } return "" } function o(e, t, a) { var o = r.disableForced4SpacesIndentedSublists ? /^ ?\d+\.[ \t]/gm : /^ {0,3}\d+\.[ \t]/gm, i = r.disableForced4SpacesIndentedSublists ? /^ ?[*+-][ \t]/gm : /^ {0,3}[*+-][ \t]/gm, l = "ul" === t ? o : i, c = ""; if (-1 !== e.search(l)) !function r(u) { var d = u.search(l), p = s(e, t); -1 !== d ? (c += "\n\n<" + t + p + ">\n" + n(u.slice(0, d), !!a) + "</" + t + ">\n", l = "ul" === (t = "ul" === t ? "ol" : "ul") ? o : i, r(u.slice(d))) : c += "\n\n<" + t + p + ">\n" + n(u, !!a) + "</" + t + ">\n" }(e); else { var u = s(e, t); c = "\n\n<" + t + u + ">\n" + n(e, !!a) + "</" + t + ">\n" } return c } return e = t.converter._dispatch("lists.before", e, r, t), e += "¨0", e = t.gListLevel ? e.replace(/^(( {0,3}([*+-]|\d+[.])[ \t]+)[^\r]+?(¨0|\n{2,}(?=\S)(?![ \t]*(?:[*+-]|\d+[.])[ \t]+)))/gm, function (e, r, t) { return o(r, t.search(/[*+-]/g) > -1 ? "ul" : "ol", !0) }) : e.replace(/(\n\n|^\n?)(( {0,3}([*+-]|\d+[.])[ \t]+)[^\r]+?(¨0|\n{2,}(?=\S)(?![ \t]*(?:[*+-]|\d+[.])[ \t]+)))/gm, function (e, r, t, a) { return o(t, a.search(/[*+-]/g) > -1 ? "ul" : "ol", !1) }), e = e.replace(/¨0/, ""), e = t.converter._dispatch("lists.after", e, r, t) }), a.subParser("metadata", function (e, r, t) { "use strict"; function a(e) { t.metadata.raw = e, (e = (e = e.replace(/&/g, "&amp;").replace(/"/g, "&quot;")).replace(/\n {4}/g, " ")).replace(/^([\S ]+): +([\s\S]+?)$/gm, function (e, r, a) { return t.metadata.parsed[r] = a, "" }) } return r.metadata ? (e = t.converter._dispatch("metadata.before", e, r, t), e = e.replace(/^\s*«««+(\S*?)\n([\s\S]+?)\n»»»+\n/, function (e, r, t) { return a(t), "¨M" }), e = e.replace(/^\s*---+(\S*?)\n([\s\S]+?)\n---+\n/, function (e, r, n) { return r && (t.metadata.format = r), a(n), "¨M" }), e = e.replace(/¨M/g, ""), e = t.converter._dispatch("metadata.after", e, r, t)) : e }), a.subParser("outdent", function (e, r, t) { "use strict"; return e = t.converter._dispatch("outdent.before", e, r, t), e = e.replace(/^(\t|[ ]{1,4})/gm, "¨0"), e = e.replace(/¨0/g, ""), e = t.converter._dispatch("outdent.after", e, r, t) }), a.subParser("paragraphs", function (e, r, t) { "use strict"; for (var n = (e = (e = (e = t.converter._dispatch("paragraphs.before", e, r, t)).replace(/^\n+/g, "")).replace(/\n+$/g, "")).split(/\n{2,}/g), s = [], o = n.length, i = 0; i < o; i++) { var l = n[i]; l.search(/¨(K|G)(\d+)\1/g) >= 0 ? s.push(l) : l.search(/\S/) >= 0 && (l = (l = a.subParser("spanGamut")(l, r, t)).replace(/^([ \t]*)/g, "<p>"), l += "</p>", s.push(l)) } for (o = s.length, i = 0; i < o; i++) { for (var c = "", u = s[i], d = !1; /¨(K|G)(\d+)\1/.test(u);) { var p = RegExp.$1, h = RegExp.$2; c = (c = "K" === p ? t.gHtmlBlocks[h] : d ? a.subParser("encodeCode")(t.ghCodeBlocks[h].text, r, t) : t.ghCodeBlocks[h].codeblock).replace(/\$/g, "$$$$"), u = u.replace(/(\n\n)?¨(K|G)\d+\2(\n\n)?/, c), /^<pre\b[^>]*>\s*<code\b[^>]*>/.test(u) && (d = !0) } s[i] = u } return e = s.join("\n"), e = e.replace(/^\n+/g, ""), e = e.replace(/\n+$/g, ""), t.converter._dispatch("paragraphs.after", e, r, t) }), a.subParser("runExtension", function (e, r, t, a) { "use strict"; if (e.filter) r = e.filter(r, a.converter, t); else if (e.regex) { var n = e.regex; n instanceof RegExp || (n = new RegExp(n, "g")), r = r.replace(n, e.replace) } return r }), a.subParser("spanGamut", function (e, r, t) { "use strict"; return e = t.converter._dispatch("spanGamut.before", e, r, t), e = a.subParser("codeSpans")(e, r, t), e = a.subParser("escapeSpecialCharsWithinTagAttributes")(e, r, t), e = a.subParser("encodeBackslashEscapes")(e, r, t), e = a.subParser("images")(e, r, t), e = a.subParser("anchors")(e, r, t), e = a.subParser("autoLinks")(e, r, t), e = a.subParser("simplifiedAutoLinks")(e, r, t), e = a.subParser("emoji")(e, r, t), e = a.subParser("underline")(e, r, t), e = a.subParser("italicsAndBold")(e, r, t), e = a.subParser("strikethrough")(e, r, t), e = a.subParser("ellipsis")(e, r, t), e = a.subParser("hashHTMLSpans")(e, r, t), e = a.subParser("encodeAmpsAndAngles")(e, r, t), r.simpleLineBreaks ? /\n\n¨K/.test(e) || (e = e.replace(/\n+/g, "<br />\n")) : e = e.replace(/  +\n/g, "<br />\n"), e = t.converter._dispatch("spanGamut.after", e, r, t) }), a.subParser("strikethrough", function (e, r, t) { "use strict"; return r.strikethrough && (e = (e = t.converter._dispatch("strikethrough.before", e, r, t)).replace(/(?:~){2}([\s\S]+?)(?:~){2}/g, function (e, n) { return function (e) { return r.simplifiedAutoLink && (e = a.subParser("simplifiedAutoLinks")(e, r, t)), "<del>" + e + "</del>" }(n) }), e = t.converter._dispatch("strikethrough.after", e, r, t)), e }), a.subParser("stripLinkDefinitions", function (e, r, t) { "use strict"; var n = function (e, n, s, o, i, l, c) { return n = n.toLowerCase(), s.match(/^data:.+?\/.+?;base64,/) ? t.gUrls[n] = s.replace(/\s/g, "") : t.gUrls[n] = a.subParser("encodeAmpsAndAngles")(s, r, t), l ? l + c : (c && (t.gTitles[n] = c.replace(/"|'/g, "&quot;")), r.parseImgDimensions && o && i && (t.gDimensions[n] = { width: o, height: i }), "") }; return e = (e += "¨0").replace(/^ {0,3}\[(.+)]:[ \t]*\n?[ \t]*<?(data:.+?\/.+?;base64,[A-Za-z0-9+/=\n]+?)>?(?: =([*\d]+[A-Za-z%]{0,4})x([*\d]+[A-Za-z%]{0,4}))?[ \t]*\n?[ \t]*(?:(\n*)["|'(](.+?)["|')][ \t]*)?(?:\n\n|(?=¨0)|(?=\n\[))/gm, n), e = e.replace(/^ {0,3}\[(.+)]:[ \t]*\n?[ \t]*<?([^>\s]+)>?(?: =([*\d]+[A-Za-z%]{0,4})x([*\d]+[A-Za-z%]{0,4}))?[ \t]*\n?[ \t]*(?:(\n*)["|'(](.+?)["|')][ \t]*)?(?:\n+|(?=¨0))/gm, n), e = e.replace(/¨0/, "") }), a.subParser("tables", function (e, r, t) { "use strict"; function n(e) { return /^:[ \t]*--*$/.test(e) ? ' style="text-align:left;"' : /^--*[ \t]*:[ \t]*$/.test(e) ? ' style="text-align:right;"' : /^:[ \t]*--*[ \t]*:$/.test(e) ? ' style="text-align:center;"' : "" } function s(e, n) { var s = ""; return e = e.trim(), (r.tablesHeaderId || r.tableHeaderId) && (s = ' id="' + e.replace(/ /g, "_").toLowerCase() + '"'), e = a.subParser("spanGamut")(e, r, t), "<th" + s + n + ">" + e + "</th>\n" } function o(e, n) { return "<td" + n + ">" + a.subParser("spanGamut")(e, r, t) + "</td>\n" } function i(e) { var i, l = e.split("\n"); for (i = 0; i < l.length; ++i)/^ {0,3}\|/.test(l[i]) && (l[i] = l[i].replace(/^ {0,3}\|/, "")), /\|[ \t]*$/.test(l[i]) && (l[i] = l[i].replace(/\|[ \t]*$/, "")), l[i] = a.subParser("codeSpans")(l[i], r, t); var c = l[0].split("|").map(function (e) { return e.trim() }), u = l[1].split("|").map(function (e) { return e.trim() }), d = [], p = [], h = [], _ = []; for (l.shift(), l.shift(), i = 0; i < l.length; ++i)"" !== l[i].trim() && d.push(l[i].split("|").map(function (e) { return e.trim() })); if (c.length < u.length) return e; for (i = 0; i < u.length; ++i)h.push(n(u[i])); for (i = 0; i < c.length; ++i)a.helper.isUndefined(h[i]) && (h[i] = ""), p.push(s(c[i], h[i])); for (i = 0; i < d.length; ++i) { for (var g = [], m = 0; m < p.length; ++m)a.helper.isUndefined(d[i][m]), g.push(o(d[i][m], h[m])); _.push(g) } return function (e, r) { for (var t = "<table>\n<thead>\n<tr>\n", a = e.length, n = 0; n < a; ++n)t += e[n]; for (t += "</tr>\n</thead>\n<tbody>\n", n = 0; n < r.length; ++n) { t += "<tr>\n"; for (var s = 0; s < a; ++s)t += r[n][s]; t += "</tr>\n" } return t += "</tbody>\n</table>\n" }(p, _) } if (!r.tables) return e; return e = t.converter._dispatch("tables.before", e, r, t), e = e.replace(/\\(\|)/g, a.helper.escapeCharactersCallback), e = e.replace(/^ {0,3}\|?.+\|.+\n {0,3}\|?[ \t]*:?[ \t]*(?:[-=]){2,}[ \t]*:?[ \t]*\|[ \t]*:?[ \t]*(?:[-=]){2,}[\s\S]+?(?:\n\n|¨0)/gm, i), e = e.replace(/^ {0,3}\|.+\|[ \t]*\n {0,3}\|[ \t]*:?[ \t]*(?:[-=]){2,}[ \t]*:?[ \t]*\|[ \t]*\n( {0,3}\|.+\|[ \t]*\n)*(?:\n|¨0)/gm, i), e = t.converter._dispatch("tables.after", e, r, t) }), a.subParser("underline", function (e, r, t) { "use strict"; return r.underline ? (e = t.converter._dispatch("underline.before", e, r, t), e = r.literalMidWordUnderscores ? (e = e.replace(/\b___(\S[\s\S]*?)___\b/g, function (e, r) { return "<u>" + r + "</u>" })).replace(/\b__(\S[\s\S]*?)__\b/g, function (e, r) { return "<u>" + r + "</u>" }) : (e = e.replace(/___(\S[\s\S]*?)___/g, function (e, r) { return /\S$/.test(r) ? "<u>" + r + "</u>" : e })).replace(/__(\S[\s\S]*?)__/g, function (e, r) { return /\S$/.test(r) ? "<u>" + r + "</u>" : e }), e = e.replace(/(_)/g, a.helper.escapeCharactersCallback), e = t.converter._dispatch("underline.after", e, r, t)) : e }), a.subParser("unescapeSpecialChars", function (e, r, t) { "use strict"; return e = t.converter._dispatch("unescapeSpecialChars.before", e, r, t), e = e.replace(/¨E(\d+)E/g, function (e, r) { var t = parseInt(r); return String.fromCharCode(t) }), e = t.converter._dispatch("unescapeSpecialChars.after", e, r, t) }), a.subParser("makeMarkdown.blockquote", function (e, r) { "use strict"; var t = ""; if (e.hasChildNodes()) for (var n = e.childNodes, s = n.length, o = 0; o < s; ++o) { var i = a.subParser("makeMarkdown.node")(n[o], r); "" !== i && (t += i) } return t = t.trim(), t = "> " + t.split("\n").join("\n> ") }), a.subParser("makeMarkdown.codeBlock", function (e, r) { "use strict"; var t = e.getAttribute("language"), a = e.getAttribute("precodenum"); return "```" + t + "\n" + r.preList[a] + "\n```" }), a.subParser("makeMarkdown.codeSpan", function (e) { "use strict"; return "`" + e.innerHTML + "`" }), a.subParser("makeMarkdown.emphasis", function (e, r) { "use strict"; var t = ""; if (e.hasChildNodes()) { t += "*"; for (var n = e.childNodes, s = n.length, o = 0; o < s; ++o)t += a.subParser("makeMarkdown.node")(n[o], r); t += "*" } return t }), a.subParser("makeMarkdown.header", function (e, r, t) { "use strict"; var n = new Array(t + 1).join("#"), s = ""; if (e.hasChildNodes()) { s = n + " "; for (var o = e.childNodes, i = o.length, l = 0; l < i; ++l)s += a.subParser("makeMarkdown.node")(o[l], r) } return s }), a.subParser("makeMarkdown.hr", function () { "use strict"; return "---" }), a.subParser("makeMarkdown.image", function (e) { "use strict"; var r = ""; return e.hasAttribute("src") && (r += "![" + e.getAttribute("alt") + "](", r += "<" + e.getAttribute("src") + ">", e.hasAttribute("width") && e.hasAttribute("height") && (r += " =" + e.getAttribute("width") + "x" + e.getAttribute("height")), e.hasAttribute("title") && (r += ' "' + e.getAttribute("title") + '"'), r += ")"), r }), a.subParser("makeMarkdown.links", function (e, r) { "use strict"; var t = ""; if (e.hasChildNodes() && e.hasAttribute("href")) { var n = e.childNodes, s = n.length; t = "["; for (var o = 0; o < s; ++o)t += a.subParser("makeMarkdown.node")(n[o], r); t += "](", t += "<" + e.getAttribute("href") + ">", e.hasAttribute("title") && (t += ' "' + e.getAttribute("title") + '"'), t += ")" } return t }), a.subParser("makeMarkdown.list", function (e, r, t) { "use strict"; var n = ""; if (!e.hasChildNodes()) return ""; for (var s = e.childNodes, o = s.length, i = e.getAttribute("start") || 1, l = 0; l < o; ++l)if (void 0 !== s[l].tagName && "li" === s[l].tagName.toLowerCase()) { n += ("ol" === t ? i.toString() + ". " : "- ") + a.subParser("makeMarkdown.listItem")(s[l], r), ++i } return (n += "\n\x3c!-- --\x3e\n").trim() }), a.subParser("makeMarkdown.listItem", function (e, r) { "use strict"; for (var t = "", n = e.childNodes, s = n.length, o = 0; o < s; ++o)t += a.subParser("makeMarkdown.node")(n[o], r); return /\n$/.test(t) ? t = t.split("\n").join("\n    ").replace(/^ {4}$/gm, "").replace(/\n\n+/g, "\n\n") : t += "\n", t }), a.subParser("makeMarkdown.node", function (e, r, t) { "use strict"; t = t || !1; var n = ""; if (3 === e.nodeType) return a.subParser("makeMarkdown.txt")(e, r); if (8 === e.nodeType) return "\x3c!--" + e.data + "--\x3e\n\n"; if (1 !== e.nodeType) return ""; switch (e.tagName.toLowerCase()) { case "h1": t || (n = a.subParser("makeMarkdown.header")(e, r, 1) + "\n\n"); break; case "h2": t || (n = a.subParser("makeMarkdown.header")(e, r, 2) + "\n\n"); break; case "h3": t || (n = a.subParser("makeMarkdown.header")(e, r, 3) + "\n\n"); break; case "h4": t || (n = a.subParser("makeMarkdown.header")(e, r, 4) + "\n\n"); break; case "h5": t || (n = a.subParser("makeMarkdown.header")(e, r, 5) + "\n\n"); break; case "h6": t || (n = a.subParser("makeMarkdown.header")(e, r, 6) + "\n\n"); break; case "p": t || (n = a.subParser("makeMarkdown.paragraph")(e, r) + "\n\n"); break; case "blockquote": t || (n = a.subParser("makeMarkdown.blockquote")(e, r) + "\n\n"); break; case "hr": t || (n = a.subParser("makeMarkdown.hr")(e, r) + "\n\n"); break; case "ol": t || (n = a.subParser("makeMarkdown.list")(e, r, "ol") + "\n\n"); break; case "ul": t || (n = a.subParser("makeMarkdown.list")(e, r, "ul") + "\n\n"); break; case "precode": t || (n = a.subParser("makeMarkdown.codeBlock")(e, r) + "\n\n"); break; case "pre": t || (n = a.subParser("makeMarkdown.pre")(e, r) + "\n\n"); break; case "table": t || (n = a.subParser("makeMarkdown.table")(e, r) + "\n\n"); break; case "code": n = a.subParser("makeMarkdown.codeSpan")(e, r); break; case "em": case "i": n = a.subParser("makeMarkdown.emphasis")(e, r); break; case "strong": case "b": n = a.subParser("makeMarkdown.strong")(e, r); break; case "del": n = a.subParser("makeMarkdown.strikethrough")(e, r); break; case "a": n = a.subParser("makeMarkdown.links")(e, r); break; case "img": n = a.subParser("makeMarkdown.image")(e, r); break; default: n = e.outerHTML + "\n\n" }return n }), a.subParser("makeMarkdown.paragraph", function (e, r) { "use strict"; var t = ""; if (e.hasChildNodes()) for (var n = e.childNodes, s = n.length, o = 0; o < s; ++o)t += a.subParser("makeMarkdown.node")(n[o], r); return t = t.trim() }), a.subParser("makeMarkdown.pre", function (e, r) { "use strict"; var t = e.getAttribute("prenum"); return "<pre>" + r.preList[t] + "</pre>" }), a.subParser("makeMarkdown.strikethrough", function (e, r) { "use strict"; var t = ""; if (e.hasChildNodes()) { t += "~~"; for (var n = e.childNodes, s = n.length, o = 0; o < s; ++o)t += a.subParser("makeMarkdown.node")(n[o], r); t += "~~" } return t }), a.subParser("makeMarkdown.strong", function (e, r) { "use strict"; var t = ""; if (e.hasChildNodes()) { t += "**"; for (var n = e.childNodes, s = n.length, o = 0; o < s; ++o)t += a.subParser("makeMarkdown.node")(n[o], r); t += "**" } return t }), a.subParser("makeMarkdown.table", function (e, r) { "use strict"; var t, n, s = "", o = [[], []], i = e.querySelectorAll("thead>tr>th"), l = e.querySelectorAll("tbody>tr"); for (t = 0; t < i.length; ++t) { var c = a.subParser("makeMarkdown.tableCell")(i[t], r), u = "---"; if (i[t].hasAttribute("style")) { switch (i[t].getAttribute("style").toLowerCase().replace(/\s/g, "")) { case "text-align:left;": u = ":---"; break; case "text-align:right;": u = "---:"; break; case "text-align:center;": u = ":---:" } } o[0][t] = c.trim(), o[1][t] = u } for (t = 0; t < l.length; ++t) { var d = o.push([]) - 1, p = l[t].getElementsByTagName("td"); for (n = 0; n < i.length; ++n) { var h = " "; void 0 !== p[n] && (h = a.subParser("makeMarkdown.tableCell")(p[n], r)), o[d].push(h) } } var _ = 3; for (t = 0; t < o.length; ++t)for (n = 0; n < o[t].length; ++n) { var g = o[t][n].length; g > _ && (_ = g) } for (t = 0; t < o.length; ++t) { for (n = 0; n < o[t].length; ++n)1 === t ? ":" === o[t][n].slice(-1) ? o[t][n] = a.helper.padEnd(o[t][n].slice(-1), _ - 1, "-") + ":" : o[t][n] = a.helper.padEnd(o[t][n], _, "-") : o[t][n] = a.helper.padEnd(o[t][n], _); s += "| " + o[t].join(" | ") + " |\n" } return s.trim() }), a.subParser("makeMarkdown.tableCell", function (e, r) { "use strict"; var t = ""; if (!e.hasChildNodes()) return ""; for (var n = e.childNodes, s = n.length, o = 0; o < s; ++o)t += a.subParser("makeMarkdown.node")(n[o], r, !0); return t.trim() }), a.subParser("makeMarkdown.txt", function (e) { "use strict"; var r = e.nodeValue; return r = r.replace(/ +/g, " "), r = r.replace(/¨NBSP;/g, " "), r = a.helper.unescapeHTMLEntities(r), r = r.replace(/([*_~|`])/g, "\\$1"), r = r.replace(/^(\s*)>/g, "\\$1>"), r = r.replace(/^#/gm, "\\#"), r = r.replace(/^(\s*)([-=]{3,})(\s*)$/, "$1\\$2$3"), r = r.replace(/^( {0,3}\d+)\./gm, "$1\\."), r = r.replace(/^( {0,3})([+-])/gm, "$1\\$2"), r = r.replace(/]([\s]*)\(/g, "\\]$1\\("), r = r.replace(/^ {0,3}\[([\S \t]*?)]:/gm, "\\[$1]:") }); "function" == typeof define && define.amd ? define(function () { "use strict"; return a }) : "undefined" != typeof module && module.exports ? module.exports = a : this.showdown = a }).call(this);
//
/* CalendarControl */
function CalendarControl(){const r=new Date,o={localDate:new Date,prevMonthLastDate:null,calWeekDays:["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],calMonthName:["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],daysInMonth:function(e,t){return new Date(t,e,0).getDate()},firstDay:function(){return new Date(r.getFullYear(),r.getMonth(),1)},lastDay:function(){return new Date(r.getFullYear(),r.getMonth()+1,0)},firstDayNumber:function(){return o.firstDay().getDay()+1},lastDayNumber:function(){return o.lastDay().getDay()+1},getPreviousMonthLastDate:function(){return new Date(r.getFullYear(),r.getMonth(),0).getDate()},navigateToPreviousMonth:function(){r.setMonth(r.getMonth()-1);o.attachEventsOnNextPrev()},navigateToNextMonth:function(){r.setMonth(r.getMonth()+1);o.attachEventsOnNextPrev()},navigateToCurrentMonth:function(){var e=o.localDate.getMonth(),t=o.localDate.getFullYear();r.setMonth(e);r.setYear(t);o.attachEventsOnNextPrev()},displayYear:function(){let e=document.querySelector(".calendar .calendar-year-label");e.innerHTML=r.getFullYear()},displayMonth:function(){let e=document.querySelector(".calendar .calendar-month-label");e.innerHTML=o.calMonthName[r.getMonth()]},selectDate:function(e){setHQTCalendar(e.target.textContent+"/"+(r.getMonth()+1)+"/"+r.getFullYear(),r.getFullYear()+"-"+(r.getMonth()+1)+"-"+e.target.textContent);},plotSelectors:function(){document.querySelector(".calendar").innerHTML+=`<div class="calendar-inner"><div class="calendar-controls"><div class="calendar-prev"><a href="#"><svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128"><path fill="#666" d="M88.2 3.8L35.8 56.23 28 64l7.8 7.78 52.4 52.4 9.78-7.76L45.58 64l52.4-52.4z"/></svg></a></div><div class="calendar-year-month"><div class="calendar-month-label"></div><div>-</div><div class="calendar-year-label"></div></div><div class="calendar-next"><a href="#"><svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128"><path fill="#666" d="M38.8 124.2l52.4-52.42L99 64l-7.77-7.78-52.4-52.4-9.8 7.77L81.44 64 29 116.42z"/></svg></a></div></div><div class="calendar-today-date">Today: ${o.calWeekDays[o.localDate.getDay()]}, ${o.localDate.getDate()}, ${o.calMonthName[o.localDate.getMonth()]} ${o.localDate.getFullYear()}</div><div class="calendar-body"></div></div>`},plotDayNames:function(){for(let e=0;e<o.calWeekDays.length;e++)document.querySelector(".calendar .calendar-body").innerHTML+=`<div>${o.calWeekDays[e]}</div>`},plotDates:function(){document.querySelector(".calendar .calendar-body").innerHTML="";o.plotDayNames();o.displayMonth();o.displayYear();let t=1,a=0,n=(o.prevMonthLastDate=o.getPreviousMonthLastDate(),[]);var l=o.daysInMonth(r.getMonth()+1,r.getFullYear());for(let e=1;e<l;e++)if(e<o.firstDayNumber()){a+=1;document.querySelector(".calendar .calendar-body").innerHTML+='<div class="prev-dates"></div>';n.push(o.prevMonthLastDate--)}else document.querySelector(".calendar .calendar-body").innerHTML+=`<div class="number-item" data-num=${t}><a class="dateNumber" href="#">${t++}</a></div>`;for(let e=0;e<a+1;e++)document.querySelector(".calendar .calendar-body").innerHTML+=`<div class="number-item" data-num=${t}><a class="dateNumber" href="#">${t++}</a></div>`;o.highlightToday();o.plotPrevMonthDates(n);o.plotNextMonthDates()},attachEvents:function(){let e=document.querySelector(".calendar .calendar-prev a"),t=document.querySelector(".calendar .calendar-next a"),a=document.querySelector(".calendar .calendar-today-date"),n=document.querySelectorAll(".calendar .dateNumber");e.addEventListener("click",o.navigateToPreviousMonth);t.addEventListener("click",o.navigateToNextMonth);a.addEventListener("click",o.navigateToCurrentMonth);for(var l=0;l<n.length;l++)n[l].addEventListener("click",o.selectDate,!1)},highlightToday:function(){var e=o.localDate.getMonth()+1,t=r.getMonth()+1;o.localDate.getFullYear()===r.getFullYear()&&e===t&&document.querySelectorAll(".number-item")&&document.querySelectorAll(".number-item")[r.getDate()-1].classList.add("calendar-today")},plotPrevMonthDates:function(t){t.reverse();for(let e=0;e<t.length;e++)document.querySelectorAll(".prev-dates")&&(document.querySelectorAll(".prev-dates")[e].textContent=t[e])},plotNextMonthDates:function(){var e=document.querySelector(".calendar-body").childElementCount;if(42<e){var t=49-e;o.loopThroughNextDays(t)}if(35<e&&e<=42)o.loopThroughNextDays(42-e)},loopThroughNextDays:function(t){if(0<t)for(let e=1;e<=t;e++)document.querySelector(".calendar-body").innerHTML+=`<div class="next-dates">${e}</div>`},attachEventsOnNextPrev:function(){o.plotDates();o.attachEvents()},init:function(){o.plotSelectors();o.plotDates();o.attachEvents()}};o.init()};
/* */

bot_avatar_default = "data:image/png;base64,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";
bot_avatar = "data:image/png;base64,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";
webchat_container = `<div class="container"><div class="hqtwidget"><div class="chat_header"><span class="chat_header_title"><img src="${bot_avatar_default}" class="chat-logo"></span><span class="chat-name">ChatBot</span><span class="hqtdropdown-trigger" href="javascript:void(0)" mydata-target="hqtdropdown" title="More menu"><i class="fas fa-ellipsis-v"></i></span><span class="close-menu" id="normal" style="display:none" title="Normal"><i class="far fa-window-restore"></i></span><span class="close-menu" id="maximize" title="Maximize"><i class="far fa-window-maximize"></i></span><span class="close-menu" id="close" title="Minimize"><i class="far fa-window-minimize"></i></span><ul id="hqtdropdown" class="hqtdropdown-content"><li><a href="javascript:void(0)" id="clear">Clear</a></li><li><a href="javascript:void(0)" id="restart">Restart</a></li></ul></div><div class="chats" id="chats"><div class="clearfix"></div></div><div class="keypad"><span id="hqttooltiptext" class="tooltiptext">Tooltip text</span><input id="userInput" placeholder="Taip mesej..." class="usrInput"></input><div id="sendButton"><i class="fas fa-paper-plane"></i></div></div></div><div class="profile_div" id="profile_div"><img class="imgProfile" src='data:image/png;base64,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'/></div></div>`;

//botTyping
function hideBotTyping() {
  $("#botAvatar").remove();
  $(".botTyping").remove();
}
function showBotTyping() {
  const botTyping = '<img class="botAvatar" id="botAvatar" src="'+bot_avatar+'"/><div class="botTyping"><div class="bounce1"></div><div class="bounce2"></div><div class="bounce3"></div></div>';
  $(botTyping).appendTo(".chats");
  $(".botTyping").show();
  scrollToBottomOfResults();
}

function askUserInfo(action) {
  showBotTyping();
  send(action);
}
//End botTyping
// cards carousel
paginated_cards_id = 0
cacheResponse = {}
historyAction = []
function createCardsCarousel(cardsData) {
	let cards = "";
	const cardsDataLength = cardsData.length;
	for (let i = 0; i < cardsDataLength; i += 1) 
	{
		let itemButton = ``;
		if(typeof cardsData[i].button != undefined)
		{
			const buttonLength = cardsData[i].button.length;
			for (let j = 0; j < buttonLength; j += 1) 
			{
				itemButton += `<div class="menuChips" data-payload='${cardsData[i].button[j].payload}'>${cardsData[i].button[j].title}</div>`;
			}
			itemButton = `<div class="menu">${itemButton}</div>`;
		}
		else 
		{
			let itemButton = '';
		}
		let item = `<div class="carousel_cards in-left"><img class="cardBackgroundImage" src=${cardsData[i].image}><div class="cardFooter"> <span class="cardTitle" title=""><span>${cardsData[i].title}<span>${itemButton}</span></div></div>`;
        cards += item;
	}
    const cardContents = `<div id="paginated_cards_${paginated_cards_id}" class="cards"> <div id="cards_scroller_${paginated_cards_id}" class="cards_scroller">${cards} <span id="prev_${paginated_cards_id}" class="arrow prev fa fa-chevron-circle-left "></span> <span id="next_${paginated_cards_id}" class="arrow next fa fa-chevron-circle-right" ></span> </div> </div>`;
    return cardContents;
}

function showCardsCarousel(cardsToAdd) {
    const cards = createCardsCarousel(cardsToAdd);
    $(cards).appendTo(".chats").show();
    if (cardsToAdd.length <= 2) {
        $(`.cards_scroller>div.carousel_cards:nth-of-type(2)`).fadeIn(1000);
    } else {
        for (let i = 0; i < cardsToAdd.length; i += 1) {
            $(`.cards_scroller>div.carousel_cards:nth-of-type(${i})`).fadeIn(1000);
        }
        $(".cards .arrow.prev").fadeIn("1000");
        $(".cards .arrow.next").fadeIn("1000");
    }
    scrollToBottomOfResults();
    const card = document.querySelector("#paginated_cards_"+paginated_cards_id);
    const card_scroller = card.querySelector("#cards_scroller_"+paginated_cards_id);
    const card_item_size = 225;
    function scrollToNextPage(h) {
        card_scroller.scrollBy({top:0, left:card_item_size + 35, behavior: 'smooth'});		
    }
    function scrollToPrevPage() {
        card_scroller.scrollBy({top:0, left:-card_item_size - 35, behavior: 'smooth'});
    }
    card.querySelector("#next_"+paginated_cards_id).addEventListener("click", scrollToNextPage);
    card.querySelector("#prev_"+paginated_cards_id).addEventListener("click", scrollToPrevPage);
	paginated_cards_id+=1;
    $(".usrInput").focus();
}
//end cards carousel

// Collapsible
function createCollapsible(collapsible_data) {
    let collapsible_list = "";
    for (let i = 0; i < collapsible_data.length; i += 1) {
        let collapsible_list_item = "";
        for (let j = 0; j < collapsible_data[i].items.length; j += 1) {
            const collapsible_item = `<p class='collapsible-item' data-payload='${collapsible_data[i].items[j].payload}' title="${collapsible_data[i].items[j].payload=="" ? "Unavailable" : "Available"}" style="${collapsible_data[i].items[j].payload=="" ? "cursor:default" : "cursor:pointer;font-weight:bold"}">${collapsible_data[i].items[j].title}</p>`;
            collapsible_list_item += collapsible_item;
        }
        const block = `<li ${i==0 ? "class='active'" : ""}><div class="collapsible-header" >${collapsible_data[i].title}</div><div class="collapsible-body">${collapsible_list_item}</div></li>`;
        collapsible_list += block;
    }
    const collapsible_contents = `<ul class="collapsible">${collapsible_list}</ul>`;
    $(collapsible_contents).appendTo(".chats");
    $(".collapsible").collapsible();
    scrollToBottomOfResults();
}
$(document).on("click", ".collapsible-item", function () {
    const payload = this.getAttribute("data-payload");
    if (payload == "") return;
    const text = this.innerText;
    setUserResponse(text);
    send(payload);
    $("#userInput").prop('disabled', false);
    $(".collapsible").remove();
  });
// end Collapsible 
//DropDown
function renderDropDwon(drop_down_data) {
    let drop_down_options = "";
    for (let i = 0; i < drop_down_data.length; i += 1) {
        drop_down_options += `<option value="${drop_down_data[i].value}">${drop_down_data[i].label}</option>`;
    }
    const drop_down_select = `<div class="dropDownMsg"><select class="browser-default dropDownSelect"> <option value="" disabled selected>Choose your option</option>${drop_down_options}</select></div>`;
    $(".chats").append(drop_down_select);
    scrollToBottomOfResults();
    $("select").on("change", function () {
        let value = "";
        let label = "";
        $("select option:selected").each(() => {
            label += $(this).val();
            value += $(this).val();
        });
        setUserResponse(label);
        send(value);
        $(".dropDownMsg").remove();
    });
}
//End Dropdown

// pdfAttchament
function renderPdfAttachment(pdf_data) {
    const { url: pdf_url } = pdf_data.custom;
    const { title: pdf_title } = pdf_data.custom;
    const pdf_attachment = `<div class="pdf_attachment"><div class="row"><div class="col s3 pdf_icon"><i class="fa fa-file-pdf-o" aria-hidden="true"></i></div><div class="col s9 pdf_link"><a href="${pdf_url}" target="_blank">${pdf_title} </a></div></div></div>`;
    $(".chats").append(pdf_attachment);
    scrollToBottomOfResults();
}
// end pdfAttachment
// QuickReplies
function showQuickReplies(quickRepliesData, autodelete = true) {
    let chips = "";
    for (let i = 0; i < quickRepliesData.length; i += 1) {
        const chip = `<div class="chipButton" data-payload='${quickRepliesData[i].payload}'>${quickRepliesData[i].title}</div>`;
        chips += chip;
    }
    var isdel = "1";
    if(autodelete == true)
    {
      isdel = "";
    }
    const quickReplies = `<div id="quickReplies${isdel}" class="quickReplies">${chips}</div><div class="clearfix"></div>`;
    $(quickReplies).appendTo(".chats").fadeIn(500);
    scrollToBottomOfResults();
    const slider = document.querySelector(".quickReplies");
    let isDown = false;
    let startX;
    let scrollLeft;
    slider.addEventListener("mousedown", (e) => {
        isDown = true;
        slider.classList.add("active");
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
    });
    slider.addEventListener("mouseleave", () => {
        isDown = false;
        slider.classList.remove("active");
    });
    slider.addEventListener("mouseup", () => {
        isDown = false;
        slider.classList.remove("active");
    });
    slider.addEventListener("mousemove", (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - slider.offsetLeft;
        const walk = (x - startX) * 3; //scroll-fast
        slider.scrollLeft = scrollLeft - walk;
    });
}
$(document).on("click", ".quickReplies .chipButton", function () {
    const text = this.innerText;
    const payload = this.getAttribute("data-payload");
    //console.log("chipButton payload: ", this.getAttribute("data-payload"));
    setUserResponse(text);
    send(payload);
    $("#quickReplies").remove();
});
// End QuickReplies
// suggestionButtons
menu_suggestions_id = 0
function addSuggestion(suggestions,sub_text="",autodelete = true) {
  setTimeout(() => {
      if (sub_text != "") {
        sub_text = '<span class="botMsg" style="margin-left:30px">'+sub_text+'</span><div class="clearfix"></div>';
      }
      const suggLength = suggestions.length;
      var isdel = "1";
      if(autodelete == true)
      {
        isdel = "";
      }
      $(
          sub_text+`<div class="singleCard"> <div id="suggestions${isdel}" class="suggestions"><div class="menu_suggestions_`+menu_suggestions_id+`"></div></div></div>`,
      ).appendTo(".chats").hide().fadeIn(500);
  
      for (let i = 0; i < suggLength; i += 1) {
        if (typeof suggestions[i].item != "undefined") {
          childButton = suggestions[i].item;
          childButtonLeng = childButton.length;
          childButtonWidth = 100/childButtonLeng;
          sub_menu_suggestions = "";
          for (let j = 0; j < childButtonLeng; j += 1) 
          {
            image_url = ""
            if(typeof childButton[j].icon != "undefined")
            {
              image_url = '<img src="'+childButton[j].icon+'" width="30" height="30">';
              sub_menu_suggestions +=`<div style="display:inline-block;width:${childButtonWidth}%;padding:3px;margin-bottom:2px"><div class="menuChips" data-payload='${childButton[j].payload}'>${image_url}<span>${childButton[j].title}</span></div></div>`;
            }
            else
            {
              sub_menu_suggestions +=`<div style="display:inline-block;width:${childButtonWidth}%;padding:3px;margin-bottom:2px"><div class="menuChips" data-payload='${childButton[j].payload}'>${childButton[j].title}</div></div>`;
            }
          }
          $(
            `<div class="sub_menu_suggestions" style="margin:0px">`+sub_menu_suggestions+`</div>`,
          ).appendTo(".menu_suggestions_"+menu_suggestions_id);
        }
        else
        {
          bgColor = ""
          if(typeof suggestions[i].bg_color != "undefined")
          {
            bgColor = "style='background: "+suggestions[i].bg_color + ";color: "+ suggestions[i].color+"'"
          }
          
          image_url = ""
          if(typeof suggestions[i].icon != "undefined")
          {
            image_url = '<img src="'+suggestions[i].icon+'" width="30" height="30">';
            $(
              `<div class="menuChips" ${bgColor} data-payload='${suggestions[i].payload}' style="height: 40px;">${image_url}<span>${suggestions[i].title}</span></div>`,
            ).appendTo(".menu_suggestions_"+menu_suggestions_id);
          }
          else
          {
            $(
              `<div class="menuChips" ${bgColor} data-payload='${suggestions[i].payload}'>${suggestions[i].title}</div>`,
            ).appendTo(".menu_suggestions_"+menu_suggestions_id);
          }
        }
      }
  
      $(document).on("click", ".menu_suggestions_"+menu_suggestions_id+" .menuChips", function () {
        const text = this.innerText;
        const payload = this.getAttribute("data-payload");
        if (payload.includes("http"))
        {
          window.open(payload);
        }
        else
        {
          setUserResponse(text);
          send(payload);
        }
        $("#suggestions").remove();
      });
    menu_suggestions_id+=1;
    scrollToBottomOfResults();
  }, 200);
}

$(document).on("click", ".menu .menuChips", function () {
    const text = this.innerText;
    const payload = this.getAttribute("data-payload");    
    if (payload.includes("http"))
    {
      window.open(payload);
    }
    else
    {
      setUserResponse(text);
      send(payload);
    }
    $(".suggestions").remove();
});
// end suggesstionButtons
// YesNoBlock
var yesnoEntities = [];
var yesnoQuestions = [];
var yesnoSubEntities = {};
var yesnoSubQuestions = {};
var yesno_page = 0;
var yesno_range = 3;
var yesno_position = 0;
function addYesNoBlock(blockData, payload, pageRange=3) {
    yesno_page = 0;
    yesno_position = 0;
    $(".yesnoblock").remove();
    yesnoEntities = [];
    yesnoQuestions = [];
    yesno_range = pageRange
    let rows = "";
    for (let i = 0; i < blockData.length; i += 1) {
        var is_display = 'flex';
        if (i<yesno_range)
        {
          is_display="flex";
        }
        else{
          is_display="none";
        }
        let row = `<div class="row" id="yesnorow${i}" style="display:${is_display}"><div class="question">${blockData[i].title}</div><div class="option"><input class="rounded-checkbox" name="${blockData[i].entity}" type="radio" value="true" onclick="showSubQuestion('yesnosubrow${i}')"/></div><div class="option"><input class="rounded-checkbox" name="${blockData[i].entity}" type="radio" value="false" checked onclick="hideSubQuestion('yesnosubrow${i}')"/></div></div>`;
        let subrow = `<div class="subrow" id="yesnosubrow${i}" style="display:none">`;
        if (blockData[i].subquestion != undefined)
        {
          var yesnoTmpEntities = [];
          var yesnoTmpQuestions = [];
          for (let j = 0; j < blockData[i].subquestion.length; j += 1) {
            if(blockData[i].subquestion[j].input != undefined)
            {
              input = blockData[i].subquestion[j].input;
              continue;
            }
            const tmprow = `<div class="row"><div class="question">+ ${blockData[i].subquestion[j].title}</div><div class="option"><input class="rounded-checkbox" onclick="removeCheckYesNo('${input}','${blockData[i].subquestion[j].entity}','${blockData[i].entity}')" name="${blockData[i].subquestion[j].entity}" type="radio" value="true"/></div><div class="option"><input class="rounded-checkbox" name="${blockData[i].subquestion[j].entity}" type="radio" value="false" checked/></div></div>`;
            subrow += tmprow;
            yesnoTmpEntities.push(blockData[i].subquestion[j].entity);
            yesnoTmpQuestions.push(blockData[i].subquestion[j].title);
          }
          yesnoSubEntities[blockData[i].entity] = yesnoTmpEntities;
          yesnoSubQuestions[blockData[i].entity] = yesnoTmpQuestions;
        }
        subrow +="</div>"
        rows += row+subrow;
        yesnoEntities.push(blockData[i].entity);
        yesnoQuestions.push(blockData[i].title);
    }
    rows+=`<div class="row_footer"><a class="button_css" id="yesnobuttonBack" onclick="backYesNo('${blockData.length}')" style="display:none">Back</a><a class="button_css" id="yesnobuttonNext" onclick="nextYesNo('${blockData.length}')">Next</a><a class="button_css" id="yesnobuttonSubmit" onclick="sendYesNo('${payload}')">submit</a></div>`;
    
    $(`<div class="yesnoblock"><div class="row" style="height: 30px"><div class="question"><p>&nbsp;</p></div><div class="option">Yes</div><div class="option">No</div></div>`+rows+`</div>`).appendTo(".chats").hide().fadeIn(500);
    
    if(yesno_range < blockData.length) 
    {
      $("#yesnobuttonNext").show();
      $("#yesnobuttonSubmit").hide();
    }
    else 
    {
      $("#yesnobuttonNext").hide();
      $("#yesnobuttonSubmit").show();
    }
    scrollToBottomOfResults();
}

function removeCheckYesNo(input, cur_entity, entity) {
  if(input == "radio")
  {
    yesnoTmpEntities = yesnoSubEntities[entity];
    for (let i = 0; i < yesnoTmpEntities.length; i += 1) {
      if(yesnoTmpEntities[i] == cur_entity) continue;
      $("input[name="+yesnoTmpEntities[i]+"][value='true']").prop('checked', false);
      $("input[name="+yesnoTmpEntities[i]+"][value='false']").prop('checked', true);
    }
  }
}

function backYesNo(length) {
  for (let i = yesno_page*yesno_range; i < yesno_page*yesno_range+yesno_range && i<length; i += 1) {
    $("#yesnorow"+i).hide();
    $("#yesnosubrow"+i).hide();
  }
  yesno_page-=1;
  for (let i = yesno_page*yesno_range; i < yesno_page*yesno_range+yesno_range && i<length; i += 1) {
    $("#yesnorow"+i).show();
    yesno_position = i;
  }
  if(yesno_position <= yesno_range) $("#yesnobuttonBack").hide();
  else $("#yesnobuttonBack").show();
  
  if(yesno_position < length) 
  {
    $("#yesnobuttonNext").show();
    $("#yesnobuttonSubmit").hide();
  }
  else 
  {
    $("#yesnobuttonNext").hide();
    $("#yesnobuttonSubmit").show();
  }
}

function nextYesNo(length) {
  for (let i = yesno_page*yesno_range; i < yesno_page*yesno_range+yesno_range && i<length; i += 1) {
    $("#yesnorow"+i).hide();
    $("#yesnosubrow"+i).hide();
  }
  yesno_page+=1;
  for (let i = yesno_page*yesno_range; i < yesno_page*yesno_range+yesno_range && i<length; i += 1) {
    $("#yesnorow"+i).show();
    yesno_position = i;
  }
  if(yesno_position <= yesno_range) $("#yesnobuttonBack").hide();
  else $("#yesnobuttonBack").show();
  
  if(yesno_position < length-1) 
  {
    $("#yesnobuttonNext").show();
    $("#yesnobuttonSubmit").hide();
  }
  else 
  {
    $("#yesnobuttonNext").hide();
    $("#yesnobuttonSubmit").show();
  }
}

function showSubQuestion(id) {
  $('#'+id).show(500, function() {
    scrollToBottomOfResults();
  });
}

function hideSubQuestion(id) {
  $('#'+id).hide(500);
  scrollToBottomOfResults();
}

function sendYesNo(payload) {
  var entities = "{";
  var user_select = "";
  for (let i = 0; i < yesnoEntities.length; i++) {
    var value = $('input[name='+yesnoEntities[i]+']:checked').val();
    entities += '"'+yesnoEntities[i]+'": "'+value+'",';
    
    if(value == 'true' && yesnoSubEntities[yesnoEntities[i]] != undefined )
    {
      for (let j = 0; j < yesnoSubEntities[yesnoEntities[i]].length; j++) {
        var subvalue = $('input[name='+yesnoSubEntities[yesnoEntities[i]][j]+']:checked').val();
        entities += '"'+yesnoSubEntities[yesnoEntities[i]][j]+'": "'+subvalue+'",';
        if (subvalue == "false"){
          subvalue = "No" ;
        }

        else {
          subvalue ="Yes";
        }
        user_select += "+ "+yesnoSubQuestions[yesnoEntities[i]][j]+": "+subvalue+"</br>";
      }
      
    }
    if (value == "false"){
      value = "No" ;
    }

    else {
      value ="Yes";
    }
    user_select += "- "+yesnoQuestions[i]+": "+value+"</br>";

    
  }
  entities+="}";
  
  payload = payload+entities;
  setUserResponse(user_select);
  payload = payload.replace(",}","}");
  send(payload);
  $(".yesnoblock").remove();
}
// BMIBlock
function addBMIBlock(blockData,payload) {
    $(".bmiblock").remove();
    setTimeout(() => {
        $(`<div class="bmiblock"><div class="row"><div class="question">What is your weight in kilograms?</div><div class="option"><input class="input_format" id="bmi_weight" type="number" min="1" max="250" /></div></div><div class="row"><div class="question">What is your height in centimeters?</div><div class="option"><input class="input_format" id="bmi_height" type="number" min="10" max="300" /></div></div><div class="row"><div class="question" style="margin-top:7px">BMI</div><div class="option"><input class="input_format" id="bmi_value" type="number" min="10" max="300" readonly /></div></div><div class="row_footer"><a class="button_css" onclick="sendBMI('${payload}')">submit</a></div></div>`).appendTo(".chats").hide().fadeIn(500);
    scrollToBottomOfResults();
    }, 500);
}
$(document).on("keyup keypress change", "#bmi_weight", function () {
  var weight = $("#bmi_weight").val();
  var height = $("#bmi_height").val();
  var mbi = height > 0 ? weight/(height/100*height/100) : "";
  $("#bmi_value").val(round(mbi,1));
});
$(document).on("keyup keypress change", "#bmi_height", function () {
  var weight = $("#bmi_weight").val();
  var height = $("#bmi_height").val();
  var mbi = height > 0 ? weight/(height/100*height/100) : "";
  $("#bmi_value").val(round(mbi,1));
});
function sendBMI(payload) {
  gender = $('#bmi_male').is(':checked') ? 'male' : 'female';
  payload = payload+'{"bmi": "'+$('#bmi_value').val()+'"}';
  var user_select = "- Height: "+ $('#bmi_height').val()+"<br>-Weight: "+ $('#bmi_weight').val()+"<br>-BMI: "+ $('#bmi_value').val();
  setUserResponse(user_select);
  send(payload);
  $(".bmiblock").remove();
}

function round(value, exp) {
  if (typeof exp === 'undefined' || +exp === 0)
    return Math.round(value);

  value = +value;
  exp = +exp;

  if (isNaN(value) || !(typeof exp === 'number' && exp % 1 === 0))
    return NaN;

  // Shift
  value = value.toString().split('e');
  value = Math.round(+(value[0] + 'e' + (value[1] ? (+value[1] + exp) : exp)));

  // Shift back
  value = value.toString().split('e');
  return +(value[0] + 'e' + (value[1] ? (+value[1] - exp) : -exp));
}
// BodyBlock
var bodyBlockEntities = [];
var bodyBlockQuestions = [];
function addBodyBlock(blockData,payload) {
    $(".bodyblock").remove();
    bodyBlockEntities = [];
    bodyBlockQuestions = [];
    setTimeout(() => {
      for (let i = 0; i < blockData.length; i += 1) {
        bodyBlockEntities.push(blockData[i].entity);
        bodyBlockQuestions.push(blockData[i].title);
      }
      $(`<div class="bodyblock"><div class="righttext">Right</div><div class="lefttext">Left</div><input class="rounded-checkbox" style="width:25px;height: 25px; border: 3px solid black; left: 110px;top: 150px;" name="bodyblock" id="${blockData[0].entity}" value="true" type="radio" /><input class="rounded-checkbox" style=" width:25px;height: 25px; border: 3px solid black;left: 75px;top: 200px;" name="bodyblock" id="${blockData[1].entity}" value="true" type="radio" /><input class="rounded-checkbox" style=" width:25px;height: 25px; border: 3px solid black; left: 80px;top: 175px;" name="bodyblock" id="${blockData[2].entity}" value="true" type="radio" /><input class="rounded-checkbox" style=" width:25px;height: 25px; border: 3px solid black;left: 72px;top: 150px;" name="bodyblock" id="${blockData[3].entity}" value="true" type="radio" /><input class="rounded-checkbox" style="width:25px;height: 25px; border: 3px solid black; left: 55px;top: 200px;" name="bodyblock" id="${blockData[4].entity}" value="true" type="radio" /><img src="https://medibot.com.au/images/robo_img.png"><a class="button_css" onclick="sendBodyBlock('${payload}')">submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();   
    }, 100);
}

function sendBodyBlock(payload) {
  var entities = "{";
  var user_select = "";
  for (let i = 0; i < bodyBlockEntities.length; i++) {
    value = $('input[id='+bodyBlockEntities[i]+']:checked').val()
    if(value == undefined) value = false;
    entities += '"'+bodyBlockEntities[i]+'":"'+value+'",';
    if (value == "true"){
      value = "Yes" ;
    }
    else {
      value ="No";
    }
    user_select += "- "+bodyBlockQuestions[i]+": "+value+"</br>";
  }
  entities+="}";
  payload = payload+entities;
  payload = payload.replace(",}","}");
  setUserResponse(user_select);
  send(payload);
  $(".bodyblock").remove();
}

// body block for chest
var bodyBlockChestEntities = [];
var bodyBlockChestQuestions = [];
function addBodyBlockChest(blockData,payload) {
    $(".bodyblock").remove();
    bodyBlockChestEntities = [];
    bodyBlockChestQuestions = [];
    setTimeout(() => {
      for (let i = 0; i < blockData.length; i += 1) {
        bodyBlockChestEntities.push(blockData[i].entity);
        bodyBlockChestQuestions.push(blockData[i].title);
      }
      
      $(`<div class="bodyblock">
      <div class="righttext">Right</div><div class="lefttext">Left</div>
      <input class="rounded-checkbox" style="width:25px;height: 25px; border: 3px solid black;left: 109px;top: 131px;" name="bodyblockchest" id="${blockData[0].entity}" value="true" type="radio" /><input class="rounded-checkbox" style="width:25px;height: 25px; border: 3px solid black;left: 105px;top: 164px;" name="bodyblockchest" id="${blockData[1].entity}" value="true" type="radio" />
      <input class="rounded-checkbox" style="width:25px;height: 25px; border: 3px solid black;left: 97px;top: 131px;" name="bodyblockchest" id="${blockData[2].entity}" value="true" type="radio" />
      
      <img style="max-height: 76%;" src="https://medibot.com.au/images/robo_img.png"><a class="button_css" onclick="sendBodyChestBlock('${payload}')">submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();   
    }, 100);
}

function sendBodyChestBlock(payload) {
  var entities = "{";
  var user_select = "";
  for (let i = 0; i < bodyBlockChestEntities.length; i++) {
    value = $('input[id='+bodyBlockChestEntities[i]+']:checked').val()
    if(value == undefined) value = false;
    entities += '"'+bodyBlockChestEntities[i]+'":"'+value+'",';
    if (value == "true"){
      value = "Yes" ;
    }
    else {
      value ="No";
    }
    user_select += "- "+bodyBlockChestQuestions[i]+": "+value+"</br>";
  }
  entities+="}";
  payload = payload+entities;
  payload = payload.replace(",}","}");
  setUserResponse(user_select);
  send(payload);
  $("bodyblock").remove();
}


// body block for joint pain
var bodyBlockJointEntities = [];
var bodyBlockJointQuestions = [];
function addBodyBlockJoint(blockData,payload) {
    $(".bodyblock").remove();
    bodyBlockJointEntities = [];
    bodyBlockJointQuestions = [];
    setTimeout(() => {
      for (let i = 0; i < blockData.length; i += 1) {
        bodyBlockJointEntities.push(blockData[i].entity);
        bodyBlockJointQuestions.push(blockData[i].title);
      }
      
      $(`<div class="bodyblock">
     
      <input class="rounded-checkbox" style="left: 190px;top: 100px;" name="bodyblockjoint" id="${blockData[0].entity}" value="true" type="radio" /><input class="rounded-checkbox" style="left: 103px;top: 110px;" name="bodyblockjoint" id="${blockData[1].entity}" value="true" type="radio" />
      <input class="rounded-checkbox" style="left: 83px;top: 150px;color: red;" name="bodyblockjoint" id="${blockData[2].entity}" value="true" type="radio" /> <input class="rounded-checkbox" style="left: 100px;top: 190px;" name="bodyblockjoint" id="${blockData[3].entity}" value="true" type="radio" />
      
      <img style="max-height: 76%;" src="https://apnamd.ai/images/body_updated.3.jpeg"><a class="button_css" onclick="sendBodyJointBlock('${payload}')">submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();   
    }, 100);
}

function sendBodyJointBlock(payload) {
  var entities = "{";
  var user_select = "";
  for (let i = 0; i < bodyBlockJointEntities.length; i++) {
    value = $('input[id='+bodyBlockJointEntities[i]+']:checked').val()
    if(value == undefined) value = false;
    entities += '"'+bodyBlockJointEntities[i]+'":"'+value+'",';
    if (value == "true"){
      value = "Yes" ;
    }
    else {
      value ="No";
    }
    user_select += "- "+bodyBlockJointQuestions[i]+": "+value+"</br>";
  }
  entities+="}";
  payload = payload+entities;
  payload = payload.replace(",}","}");
  setUserResponse(user_select);
  send(payload);
  $("bodyblock").remove();
}



// body block for joint pain hand imG1
var bodyblockjointHandimage1_Entities = [];
var bodyblockjointHandimage1_Questions = [];
function addBodyBlockjoint_Hand_image1(blockData,payload) {
    $(".bodyblock").remove();
    bodyblockjointHandimage1_Entities = [];
    bodyblockjointHandimage1_Questions = [];
    setTimeout(() => {
      for (let i = 0; i < blockData.length; i += 1) {
        bodyblockjointHandimage1_Entities.push(blockData[i].entity);
        bodyblockjointHandimage1_Questions.push(blockData[i].title);
      }

      $(`<div class="bodyblock">
      <label style="
      margin-left: 50px; ">Yes</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top: 0px;"name="bodyblockjointHandimage1" id="${blockData[0].entity}" value="true" type="radio" /> 
      
      <label style="left: 50px;
      margin-left: 60px; ">No</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top:0px;" name="bodyblockjointHandimage1" id="${blockData[0].entity}" value="false" type="radio" /> 
      
      
      <img style="max-height: 76%;" src="https://apnamd.ai/images/RA2.png"> <a class="button_css" onclick="sendBodyJointHandimage1Block('${payload}')" >submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();   

    }, 100);
}

function sendBodyJointHandimage1Block(payload) {
  
  var entities = "{";
  var user_select = "";
  
  for (let i = 0; i < bodyblockjointHandimage1_Entities.length; i++) {
    value = $('input[id='+bodyblockjointHandimage1_Entities[i]+']:checked').val()
    
    if(value == undefined) value = false;
    entities += '"'+bodyblockjointHandimage1_Entities[i]+'":"'+value+'",';
    if (value == "true"){
      value = "Yes" ;
    }
    else {
      value ="No";
    }
    user_select += "- "+bodyblockjointHandimage1_Questions[i]+": "+value+"</br>";
  }
  entities+="}";
  payload = payload+entities;
  payload = payload.replace(",}","}");
  setUserResponse(user_select);
  send(payload);
  $("bodyblock").remove();
}


// body block for hand iamge1 part2
var bodyblockjointHandimage1_part2_Entities = [];
var bodyblockjointHandimage1_part2_Questions = [];
function addBodyBlockjoint_Hand_image1_part2(blockData,payload) {
    $(".bodyblock").remove();
    bodyblockjointHandimage1_part2_Entities = [];
    bodyblockjointHandimage1_part2_Questions = [];
    setTimeout(() => {
      for (let i = 0; i < blockData.length; i += 1) {
        bodyblockjointHandimage1_part2_Entities.push(blockData[i].entity);
        bodyblockjointHandimage1_part2_Questions.push(blockData[i].title);
      }
      
      $(`<div class="bodyblock">
      <label style="
      margin-left: 50px; ">Yes</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top: 0px;"name="bodyblockjointHandimage1_part2" id="${blockData[0].entity}" value="true" type="radio" /> 
      
      <label style="left: 50px;
      margin-left: 60px; ">No</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top:0px;" name="bodyblockjointHandimage1_part2" id="${blockData[0].entity}" value="false" type="radio" /> 
      
      <img style="max-height: 76%;" src="https://apnamd.ai/images/OA.png">
      <a class="button_css" onclick="sendBodyJointHandimage1_part2_Block('${payload}')"  >submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();   
    }, 100);
}

function sendBodyJointHandimage1_part2_Block(payload) {
  var entities = "{";
  var user_select = "";
  for (let i = 0; i < bodyblockjointHandimage1_part2_Entities.length; i++) {
    value = $('input[id='+bodyblockjointHandimage1_part2_Entities[i]+']:checked').val()
    if(value == undefined) value = false;
    entities += '"'+bodyblockjointHandimage1_part2_Entities[i]+'":"'+value+'",';
    if (value == "true"){
      value = "Yes" ;
    }
    else {
      value ="No";
    }
    user_select += "- "+bodyblockjointHandimage1_part2_Questions[i]+": "+value+"</br>";
  }
  entities+="}";
  payload = payload+entities;
  payload = payload.replace(",}","}");
  setUserResponse(user_select);
  send(payload);
  $("bodyblock").remove();
}

// body block for hand iamge1 part3
var bodyblockjointHandimage1_part3_Entities = [];
var bodyblockjointHandimage1_part3_Questions = [];
function addBodyBlockjoint_Hand_image1_part3(blockData,payload) {
    $(".bodyblock").remove();
    bodyblockjointHandimage1_part3_Entities = [];
    bodyblockjointHandimage1_part3_Questions = [];
    setTimeout(() => {
      for (let i = 0; i < blockData.length; i += 1) {
        bodyblockjointHandimage1_part3_Entities.push(blockData[i].entity);
        bodyblockjointHandimage1_part3_Questions.push(blockData[i].title);
      }
      
      $(`<div class="bodyblock">
      <label style="
      margin-left: 50px; ">Yes</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top: 0px;"name="bodyblockjointHandimage1_part3" id="${blockData[0].entity}" value="true" type="radio" /> 
      
      <label style="left: 50px;
      margin-left: 60px; ">No</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top:0px;" name="bodyblockjointHandimage1_part3" id="${blockData[0].entity}" value="false" type="radio" /> 
      
      <img style="max-height: 76%;" src="https://apnamd.ai/images/tophy.PNG">
      <a class="button_css" onclick="sendBodyJointHandimage1_part3_Block('${payload}')"  >submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();   
    }, 100);
}

function sendBodyJointHandimage1_part3_Block(payload) {
  var entities = "{";
  var user_select = "";
  for (let i = 0; i < bodyblockjointHandimage1_part3_Entities.length; i++) {
    value = $('input[id='+bodyblockjointHandimage1_part3_Entities[i]+']:checked').val()
    if(value == undefined) value = false;
    entities += '"'+bodyblockjointHandimage1_part3_Entities[i]+'":"'+value+'",';
    if (value == "true"){
      value = "Yes" ;
    }
    else {
      value ="No";
    }
    user_select += "- "+bodyblockjointHandimage1_part3_Questions[i]+": "+value+"</br>";
  }
  entities+="}";
  payload = payload+entities;
  payload = payload.replace(",}","}");
  setUserResponse(user_select);
  send(payload);
  $("bodyblock").remove();
}



// body block for joint pain hand imG2
var bodyblockjointHandimage2_Entities = [];
var bodyblockjointHandimage2_Questions = [];
function addBodyBlockjoint_Hand_image2(blockData,payload) {
    $(".bodyblock").remove();
    bodyblockjointHandimage2_Entities = [];
    bodyblockjointHandimage2_Questions = [];
    setTimeout(() => {
      for (let i = 0; i < blockData.length; i += 1) {
        bodyblockjointHandimage2_Entities.push(blockData[i].entity);
        bodyblockjointHandimage2_Questions.push(blockData[i].title);
      }

      $(`<div class="bodyblock">
      <label style="
      margin-left: 50px; ">Yes</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top: 0px;"name="bodyblockjointHandimage2" id="${blockData[0].entity}" value="true" type="radio" /> 
      
      <label style="left: 50px;
      margin-left: 60px; ">No</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top:0px;" name="bodyblockjointHandimage2" id="${blockData[0].entity}" value="false" type="radio" /> 
      
      <img style="max-height: 76%;" src="https://apnamd.ai/images/gout feet.png"> <a class="button_css" onclick="sendBodyJointHandimage2Block('${payload}')" >submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();   
    }, 100);
}

function sendBodyJointHandimage2Block(payload) {
  var entities = "{";
  var user_select = "";
  for (let i = 0; i < bodyblockjointHandimage2_Entities.length; i++) {
    value = $('input[id='+bodyblockjointHandimage2_Entities[i]+']:checked').val()
    if(value == undefined) value = false;
    entities += '"'+bodyblockjointHandimage2_Entities[i]+'":"'+value+'",';
    if (value == "true"){
      value = "Yes" ;
    }
    else {
      value ="No";
    }
    user_select += "- "+bodyblockjointHandimage2_Questions[i]+": "+value+"</br>";
  }
  entities+="}";
  payload = payload+entities;
  payload = payload.replace(",}","}");
  setUserResponse(user_select);
  send(payload);
  $("bodyblock").remove();
}



// body block for joint pain hand imG3
var bodyblockjointHandimage3_Entities = [];
var bodyblockjointHandimage3_Questions = [];
function addBodyBlockjoint_Hand_image3(blockData,payload) {
    $(".bodyblock").remove();
    bodyblockjointHandimage3_Entities = [];
    bodyblockjointHandimage3_Questions = [];
    setTimeout(() => {
      for (let i = 0; i < blockData.length; i += 1) {
        bodyblockjointHandimage3_Entities.push(blockData[i].entity);
        bodyblockjointHandimage3_Questions.push(blockData[i].title);
      }

      $(`<div class="bodyblock">
      <label style="
      margin-left: 50px; ">Yes</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top: 0px;"name="bodyblockjointHandimage3" id="${blockData[0].entity}" value="true" type="radio" /> 
      
      <label style="left: 50px;
      margin-left: 60px; ">No</label>
      <input class="rounded-checkbox" style="border: 3px solid black; ;width:25px;height: 25px;left: 0px;top:0px;" name="bodyblockjointHandimage3" id="${blockData[0].entity}" value="false" type="radio" /> 
      
      
      <img style="max-height: 76%;" src="https://apnamd.ai/images/knee.png"> <a class="button_css" onclick="sendBodyJointHandimage3Block('${payload}')"  >submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();   
    }, 100);
}

function sendBodyJointHandimage3Block(payload) {
  
  var entities = "{";
  var user_select = "";
  
  for (let i = 0; i < bodyblockjointHandimage3_Entities.length; i++) {
    value = $('input[id='+bodyblockjointHandimage3_Entities[i]+']:checked').val()
    if(value == undefined) value = false;
    entities += '"'+bodyblockjointHandimage3_Entities[i]+'":"'+value+'",';
    if (value == "true"){
      value = "Yes" ;
    }
    else {
      value ="No";
    }
    user_select += "- "+bodyblockjointHandimage3_Questions[i]+": "+value+"</br>";
  }
  entities+="}";
  payload = payload+entities;
  payload = payload.replace(",}","}");
  setUserResponse(user_select);
  send(payload);
  $("bodyblock").remove();
}


// body block for symptoms on body
var bodyblockSymptomsOnBody_Entities = [];
var bodyblockSymptomsOnBody_Questions = [];
function addBodyBlockSymptomsOnBody(blockData,payload) {
    $(".bodyblock").remove();
    bodyblockSymptomsOnBody_Entities = [];
    bodyblockSymptomsOnBody_Questions = [];
    setTimeout(() => {
      for (let i = 0; i < blockData.length; i += 1) {
        bodyblockSymptomsOnBody_Entities.push(blockData[i].entity);
        bodyblockSymptomsOnBody_Questions.push(blockData[i].title);
      }
      
      $(`<div class="bodyblock">
      <label style="
      margin-left: 50px; ">Yes</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top: 0px;"name="bodyblockSymptomsOnBody" id="${blockData[0].entity}" value="true" type="radio" /> 
      
      <label style="left: 50px;
      margin-left: 60px; ">No</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top:0px;" name="bodyblockSymptomsOnBody" id="${blockData[0].entity}" value="false" type="radio" /> 
      
      <img style="max-height: 76%;" src="https://apnamd.ai/images/RA Nodule.PNG">
      <a class="button_css" onclick="sendBodySymptomsOnBody('${payload}')"  >submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();   
    }, 100);
}

function sendBodySymptomsOnBody(payload) {
  var entities = "{";
  var user_select = "";
  for (let i = 0; i < bodyblockSymptomsOnBody_Entities.length; i++) {
    value = $('input[id='+bodyblockSymptomsOnBody_Entities[i]+']:checked').val()
    if(value == undefined) value = false;
    entities += '"'+bodyblockSymptomsOnBody_Entities[i]+'":"'+value+'",';
    if (value == "true"){
      value = "Yes" ;
    }
    else {
      value ="No";
    }
    user_select += "- "+bodyblockSymptomsOnBody_Questions[i]+": "+value+"</br>";
  }
  entities+="}";
  payload = payload+entities;
  payload = payload.replace(",}","}");
  setUserResponse(user_select);
  send(payload);
  $("bodyblock").remove();
}

// body block for symptoms on body1
var bodyblockSymptomsOnBody1_Entities = [];
var bodyblockSymptomsOnBody1_Questions = [];
function addBodyBlockSymptomsOnBody1(blockData,payload) {
    $(".bodyblock").remove();
    bodyblockSymptomsOnBody1_Entities = [];
    bodyblockSymptomsOnBody1_Questions = [];
    setTimeout(() => {
      for (let i = 0; i < blockData.length; i += 1) {
        bodyblockSymptomsOnBody1_Entities.push(blockData[i].entity);
        bodyblockSymptomsOnBody1_Questions.push(blockData[i].title);
      }
      
      $(`<div class="bodyblock">
     
      <label style="
      margin-left: 50px; ">Yes</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top: 0px;" name="bodyblockSymptomsOnBody1" id="${blockData[0].entity}" value="true" type="radio" />
      
      <label style="left: 50px;
      margin-left: 60px; ">No</label>
      <input class="rounded-checkbox" style="border: 3px solid black; width:25px;height: 25px;left: 0px;top:0px;" name="bodyblockSymptomsOnBody1" id="${blockData[0].entity}" value="false" type="radio" /> 

      <img style="max-height: 76%;margin-top: 6px;" src="https://apnamd.ai/images/psoriasis.png"> <a class="button_css" onclick="sendBodySymptomsOnBody1('${payload}')"  >submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();   
    }, 100);
}

function sendBodySymptomsOnBody1(payload) {
  var entities = "{";
  var user_select = "";
  for (let i = 0; i < bodyblockSymptomsOnBody1_Entities.length; i++) {
    value = $('input[id='+bodyblockSymptomsOnBody1_Entities[i]+']:checked').val()
    if(value == undefined) value = false;
    entities += '"'+bodyblockSymptomsOnBody1_Entities[i]+'":"'+value+'",';
    if (value == "true"){
      value = "Yes" ;
    }
    else {
      value ="No";
    }
    user_select += "- "+bodyblockSymptomsOnBody1_Questions[i]+": "+value+"</br>";
  }
  entities+="}";
  payload = payload+entities;
  payload = payload.replace(",}","}");
  setUserResponse(user_select);
  send(payload);
  $("bodyblock").remove();
}


// body block for back pain
var bodyblockbackpainEntities = [];
var bodyblockbackpainQuestions = [];
function addBodyBlockBackpain(blockData,payload) {
    $(".bodyblock").remove();
    bodyblockbackpainEntities = [];
    bodyblockbackpainQuestions = [];
    setTimeout(() => {
      for (let i = 0; i < blockData.length; i += 1) {
        bodyblockbackpainEntities.push(blockData[i].entity);
        bodyblockbackpainQuestions.push(blockData[i].title);
      }
      
      $(`<div class="bodyblock">
     
      <input class="rounded-checkbox" style="border: 3px solid black; left: 134px;top: 84px;" name="bodyblockbackpain" id="${blockData[0].entity}" value="true" type="checkbox" /><input class="rounded-checkbox" style=" border: 3px solid black;left: 107px;top: 115px;" name="bodyblockbackpain" id="${blockData[1].entity}" value="true" type="checkbox" />
      <input class="rounded-checkbox" style="border: 3px solid black;left: 86px;top: 132px;color: red;" name="bodyblockbackpain" id="${blockData[2].entity}" value="true" type="checkbox" /> <input class="rounded-checkbox" style="border: 3px solid black;left: 94px;top: 115px;" name="bodyblockbackpain" id="${blockData[3].entity}" value="true" type="checkbox" /> <input class="rounded-checkbox" style="border: 3px solid black;left: 81px;top: 174px;" name="bodyblockbackpain" id="${blockData[4].entity}" value="true" type="checkbox" />
      
      <img style="max-height: 76%;" src="https://apnamd.ai/images/back enlarged_updated2.png"><a class="button_css" onclick="SendBodyBackPainBlock('${payload}')">submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();   
    }, 100);
}

function SendBodyBackPainBlock(payload) {
  var entities = "{";
  var user_select = "";
  for (let i = 0; i < bodyblockbackpainEntities.length; i++) {
    value = $('input[id='+bodyblockbackpainEntities[i]+']:checked').val()
    if(value == undefined) value = false;
    entities += '"'+bodyblockbackpainEntities[i]+'":"'+value+'",';
    if (value == "true"){
      value = "Yes" ;
    }
    else {
      value ="No";
    }
    user_select += "- "+bodyblockbackpainQuestions[i]+": "+value+"</br>";
  }
  entities+="}";
  payload = payload+entities;
  payload = payload.replace(",}","}");
  setUserResponse(user_select);
  send(payload);
  $("bodyblock").remove();
}

// Userdatablock
function adduserdataBlock(payload) {
  setTimeout(() => {
      $(`
      <div class="userinfoblock">
      <label for="hqtfdate">Date of Birth</label>
      <input type="date" id="hqtfdate" name="hqtfdate" placeholder="Your date of Birth..">
      
      <label for="hqtfgender">Gender</label>
      <select id="hqtfgender" name="hqtfgender">
        <option value="male" selected>Male</option>
        <option value="female">Female</option>
      </select>
      
      <input type="submit" value="Submit" onclick="senduserdataBlock('${payload}')">
    </div>`).appendTo(".chats").hide().fadeIn(500);
  scrollToBottomOfResults();
  }, 100);
}

function senduserdataBlock(payload) {
var dateofbirth = $("#hqtfdate").val();
var gender = $("#hqtfgender").val();
var is_error = false;
var date = new Date(dateofbirth);
var selectDate = (date.getMonth()+1)+"/"+date.getDate()+"/"+date.getFullYear();
if(!hqtValidate("date",selectDate))
{
  $("#hqtfdate").css("border-color","red");
  is_error = true;
}
else
{
  $("#hqtfdate").css("border-color","#04AA6D");
}


if(is_error) return;

var entities = "{";
var user_select = "";

entities += '"birthday":"'+$("#hqtfdate").val()+'",';
entities += '"gender":"'+gender+'"';
user_select += "- Date of Birth: "+selectDate+"</br>";
user_select += "- Gender: "+gender+"</br>";

entities+="}";
payload = payload+entities;
setUserResponse(user_select);
send(payload);
$(".userinfoblock").remove();
}




// UserInfoBlock
function addUserInfoBlock(payload) {
    setTimeout(() => {
        $(`
        <div class="userinfoblock">
          
          <label for="hqtfemail">Email ID</label>
          <input type="text" id="hqtfemail" name="hqtfemail" placeholder="Your email..">
          
          <input type="submit" value="Submit" onclick="sendUserInfoBlock('${payload}')">
        </div>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();
    }, 100);
}

function sendUserInfoBlock(payload) {
  var email = $("#hqtfemail").val();
  var dateofbirth = $("#hqtfdate").val();
  var gender = $("#hqtfgender").val();
  var phone = $("#hqtfphone").val();
  var is_error = false;
  var date = new Date(dateofbirth);
  var selectDate = (date.getMonth()+1)+"/"+date.getDate()+"/"+date.getFullYear();
  if(!hqtValidate("date",selectDate))
  {
    $("#hqtfdate").css("border-color","red");
    // is_error = true;
  }
  else
  {
    $("#hqtfdate").css("border-color","#04AA6D");
  }
  if(!hqtValidate("email",email))
  {
    $("#hqtfemail").css("border-color","red");
    is_error = true;
  }
  else
  {
    $("#hqtfemail").css("border-color","#04AA6D");
     if(!is_error) is_error = false;
  }
  if(!hqtValidate("phone",phone))
  {
    $("#hqtfphone").css("border-color","red");
    // is_error = true;
  }
  else
  {
    $("#hqtfphone").css("border-color","#04AA6D");
    if(!is_error) is_error = false;
  }
  if(is_error) return;
  
  var entities = "{";
  var user_select = "";

  entities += '"email":"'+email+'"';
  // entities += '"birthday":"'+$("#hqtfdate").val()+'",';
  // entities += '"gender":"'+gender+'",';
  // entities += '"phone":"'+phone+'"';
  user_select += "- Email: "+email+"</br>";
  // user_select += "- Date of Birth: "+selectDate+"</br>";
  // user_select += "- Gender: "+gender+"</br>";
  // user_select += "- Phone: "+phone+"</br>";
  
  entities+="}";
  payload = payload+entities;
  setUserResponse(user_select);
  send(payload);
  $(".userinfoblock").remove();
}
// CalendarBox
var calendar_payload = "";
var calendar_entity = "";
function addCalendarBox(payload,entity) {
    setTimeout(() => {
        $(`<div class="calendar"></div>`).appendTo(".chats").hide().fadeIn(500);
        const calendarControl = new CalendarControl();
        scrollToBottomOfResults();
        calendar_payload = payload;
        calendar_entity = entity;
    }, 100);
}

function setHQTCalendar(selected_date_0,selected_date_1)
{
  setUserResponse(selected_date_0);
  var entities = '{"'+calendar_entity+'":"'+selected_date_1+'"}';
  send(calendar_payload+entities);
  $(".calendar").remove();
}
// DateBox
function addDateBox(data) {
  var date = new Date();
  var currentDate = date.getFullYear()+"-"+(date.getMonth()+1)+"-"+date.getDate();
    setTimeout(() => {
        $(`<div class="datebox"><input type="date" id="hqtdatabox" value="${currentDate}"><a id="hqtselectdatabox" class="button_css" data-payload='${data.payload}'>Submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
        
        $(document).on("click", "#hqtselectdatabox", function () {
          //const text = this.innerText;
          var date = new Date($('#hqtdatabox').val());
          var selectDate = (date.getMonth()+1)+"/"+date.getDate()+"/"+date.getFullYear();
          var payload = this.getAttribute("data-payload");
          payload = payload.replace("user_input",selectDate);
          setUserResponse(selectDate);
          send(payload);
          $(".datebox").remove();
        });
        scrollToBottomOfResults();
    }, 100);
	  
}
// TimeBox
function addTimeBox(data) {
    var date = new Date($.now());
    var currentTime = date.getHours()+":"+date.getMinutes();
    setTimeout(() => {
        $(`<div class="timebox"><input type="time" id="hqttimebox" value="${currentTime}"><a id="hqtselecttimebox" class="button_css" data-payload='${data.payload}'>Submit</a></div>`).appendTo(".chats").hide().fadeIn(500);
        $(document).on("click", "#hqtselecttimebox", function () {
          var selectedTime = $('#hqttimebox').val();
          var payload = this.getAttribute("data-payload");
          payload = payload.replace("user_input",selectedTime);
          setUserResponse(selectedTime);
          send(payload);
          $(".timebox").remove();
        });
        scrollToBottomOfResults();
    }, 100);
	  
}
// Feedback
var feedbackEntities = [];
var feedbackQuestions = [];
function addFeedBack(blockData,listDate,payload) {
    feedbackEntities = [];
    feedbackQuestions = [];
    setTimeout(() => {
        let rows = "";
        for (let i = 0; i < blockData.length; i += 1) {
            const row = `<div class="row"><div class="question">${blockData[i].title}</div><div class="option"><input class="rounded-checkbox" name="${blockData[i].entity}" type="radio" value="fair" /></div><div class="option"><input class="rounded-checkbox" name="${blockData[i].entity}" type="radio" value="good"/></div><div class="option"><input class="rounded-checkbox" name="${blockData[i].entity}" type="radio" value="excellent"/></div></div>`;
            rows += row;
            feedbackEntities.push(blockData[i].entity);
            feedbackQuestions.push(blockData[i].title);
        }
        let itemDate = ``;
        for (let i = 0; i < listDate.length; i += 1) {
          itemDate += `<option value="${listDate[i].id}">${listDate[i].datetime}</option>`
        }
        let commboDate = `<select id="feedBackAppointmentID">${itemDate}</select>`
        rows+=`<div class="row_footer"><a class="button_css" onclick="sendFeedBack('${payload}')">submit</a></div>`;
        $(`<div class="feedback"><div class="row"><div class="question"></div><div class="option">Fair</div><div class="option">Good</div><div class="option">Excellent</div></div>`+rows+`</div>`).appendTo(".chats").hide().fadeIn(500);
        scrollToBottomOfResults();
    }, 100);
	
}

function sendFeedBack(payload) {
  if($('#feedBackAppointmentID').val() == null) 
  {
    appointment_id = 0;
  }
  else
  {
    appointment_id = $('#feedBackAppointmentID').val();
  }
  var entities = "{";
  var user_select = "";
  for (let i = 0; i < feedbackEntities.length; i++) {
    value = $('input[name='+feedbackEntities[i]+']:checked').val()
    if(value == undefined) return;
    entities += '"'+feedbackEntities[i]+'":"'+value+'",';
    user_select += "- "+feedbackQuestions[i]+": "+value+"</br>";
  }
  entities+="}";
  
  payload = payload+entities;
  payload = payload.replace(",}",',"comment":"'+$('#feedBackComment').val()+'","appointment_id":"'+appointment_id+'"}');
  // user_select +="- Comment: "+$('#feedBackComment').val();
  setUserResponse(user_select);
  
  send(payload);
  $(".feedback").remove();
}

// addDurationQuestionBox
var durationPayLoad = "";
function addDurationQuestionBox(blockData,payload) {
    durationPayLoad = payload;
    setTimeout(() => {
        let rows = `<div class="durationQuestion"><div class="wrapper-progressBar"><ul class="progressBar">`;
        for (let i = 0; i < blockData.length; i += 1) {
            const row = `<li class="optionDurationQuestion item${i+1}" data-entity="${blockData[i].entity}" data-value="${blockData[i].value}">${blockData[i].title}</li>`;
            rows += row;
        }
        $(rows+`</ul></div></div>`).appendTo(".chats").hide().fadeIn(500);
        scrollToBottomOfResults();
    }, 100);
}

$(document).on("click", ".optionDurationQuestion", function () {
    const text = this.innerText;
    const entity = this.getAttribute("data-entity");
    const value = this.getAttribute("data-value");
    //this.setAttribute("class","active");
    let entities = "{";
    entities += '"'+entity+'":"'+value+'"}';
    durationPayLoad = durationPayLoad+entities;
    setUserResponse(text);
    send(durationPayLoad);
    $(".durationQuestion").remove();
});
    
// addFaceBlock
var faceEntities = [];
var faceQuestions = [];
function addFaceBlock(blockData,payload) {
  faceEntities = [];
  faceQuestions = [];
  setTimeout(() => {
      let rows = "";
      for (let i = 0; i < 1; i += 1) {
          const row = `<tr>
                        <th colspan="4" class="question">${blockData[i].title}</th>
                      </tr>
                      <tr>
                        <td class="optionFaceBlock hqticon" data-entity="${blockData[i].entity}" id="hqt1${blockData[i].entity}" value="none">😀</td>
                        <td class="optionFaceBlock hqticon" data-entity="${blockData[i].entity}" id="hqt2${blockData[i].entity}" value="somedays">🙂</td>
                        <td class="optionFaceBlock hqticon" data-entity="${blockData[i].entity}" id="hqt3${blockData[i].entity}" value="mostdays">🙁</td>
                        <td class="optionFaceBlock hqticon" data-entity="${blockData[i].entity}" id="hqt4${blockData[i].entity}" value="everydays">😞</td>
                      </tr>
                      <tr>
                        <td class="title" style="color:#000000">None</td>
                        <td class="title" style="color:#000000">Some days</td>
                        <td class="title" style="color:#000000">Most days</td>
                        <td class="title" style="color:#000000">Everyday</td>
                      </tr>`;
          rows += row;
          faceEntities.push(blockData[i].entity);
          faceQuestions.push(blockData[i].title);
      }

      for (let i = 1; i < blockData.length; i += 1) {
        const row = `<tr>
                      <th colspan="4" class="question">${blockData[i].title}</th>
                    </tr>
                    <tr>
                        <td class="optionFaceBlock hqticon" data-entity="${blockData[i].entity}" id="hqt1${blockData[i].entity}" value="none">😀</td>
                        <td class="optionFaceBlock hqticon" data-entity="${blockData[i].entity}" id="hqt2${blockData[i].entity}" value="somedays">🙂</td>
                        <td class="optionFaceBlock hqticon" data-entity="${blockData[i].entity}" id="hqt3${blockData[i].entity}" value="mostdays">🙁</td>
                        <td class="optionFaceBlock hqticon" data-entity="${blockData[i].entity}" id="hqt4${blockData[i].entity}" value="everydays">😞</td>
                      </tr>
                     `;
        rows += row;
        faceEntities.push(blockData[i].entity);
        faceQuestions.push(blockData[i].title);
    }


      $(`<table class="tableFace">`
        +rows+
        `<tr>
          <th colspan="4" class="question"><a id="hqtselecttimebox" class="button_css" onclick="sendFaceBlock('${payload}')">Submit</a></th>
        </tr>
      </table>`).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();
  }, 100);
}

$(document).on("click", ".optionFaceBlock", function () {
    const name = this.getAttribute("id");
    const entity = this.getAttribute("data-entity");
    $("#hqt1"+entity).removeClass("selected");
    $("#hqt2"+entity).removeClass("selected");
    $("#hqt3"+entity).removeClass("selected");
    $("#hqt4"+entity).removeClass("selected");
    this.classList.add("selected");
});

function sendFaceBlock(payload) {
  var entities = "{";
  var user_select = "";
  for (let i = 0; i < faceEntities.length; i++) {
    let value = "None";
    if($("#hqt1"+faceEntities[i]).hasClass("selected"))
    {
      value = $("#hqt1"+faceEntities[i]).attr("value");
    }
    if($("#hqt2"+faceEntities[i]).hasClass("selected"))
    {
      value = $("#hqt2"+faceEntities[i]).attr("value");
    }
    if($("#hqt3"+faceEntities[i]).hasClass("selected"))
    {
      value = $("#hqt3"+faceEntities[i]).attr("value");
    }
    if($("#hqt4"+faceEntities[i]).hasClass("selected"))
    {
      value = $("#hqt4"+faceEntities[i]).attr("value");
    }
    entities += '"'+faceEntities[i]+'":"'+value+'",';
    user_select += "- "+faceQuestions[i]+" "+value+"</br>";
  }
  entities+="}";
  
  payload = payload+entities;
  payload = payload.replace(",}","}");
  setUserResponse(user_select);
  
  send(payload);
  $(".tableFace").remove();
}
        
// UploadImage
function addUploadImageBox(check_type,api_url) {
  $(".hqtUploadImage").remove();
  setTimeout(() => {
    $(`<div class="hqtUploadImage"><div id="ddArea" class="ddArea">
        Drag and Drop or
        <a class="button_css">
            Select File(s)
        </a>
    </div>
    <div id="showThumb" class="message"></div>
    <input type="file" class="d-none" id="selectfile" multiple /></div>`).appendTo(".chats").hide().fadeIn(500);
    $(document).ready(function() {
      $("#ddArea").on("dragover", function() {
        $(this).addClass("drag_over");
        return false;
      });

      $("#ddArea").on("dragleave", function() {
        $(this).removeClass("drag_over");
        return false;
      });

      $("#ddArea").on("click", function(e) {
        file_explorer();
      });

      $("#ddArea").on("drop", function(e) {
        e.preventDefault();
        $(this).removeClass("drag_over");
        var formData = new FormData();
        var files = e.originalEvent.dataTransfer.files;
        for (var i = 0; i < files.length; i++) {
          formData.append("file", files[i]);
        }
        formData.append("user_id", sender_id);
        formData.append("check_type", checktype);
        uploadFormData(formData);
      });

      function file_explorer() {
        document.getElementById("selectfile").click();
        document.getElementById("selectfile").onchange = function() {
          files = document.getElementById("selectfile").files;
          var formData = new FormData();

          for (var i = 0; i < files.length; i++) {
            formData.append("file", files[i]);
          }
          formData.append("user_id", sender_id);
          formData.append("check_type", check_type);
          uploadFormData(formData);
        };
      }

      function uploadFormData(form_data) {
        $('#showThumb').hide();
        $('.chats').append('<div class="loader"></div>'); //add loader if not exist
        $('.loader').show(); // show loader
        jQuery.support.cors = true;
        $.ajax({
          url: api_url,
          method: "POST",
          data: form_data,
          cache: false,
          contentType: false,
          processData: false,
          crossDomain: true,
          success: function(data) {
            $('.loader').hide();
            $('#showThumb').text(data.Details);
            $('#showThumb').show();
            scrollToBottomOfResults();
          }
        });
      }
    });
    scrollToBottomOfResults();
  }, 100);
}
// CHAT
const converter = new showdown.Converter();
function scrollToBottomOfResults() {
  const terminalResultsDiv = document.getElementById("chats");
  terminalResultsDiv.scrollTop = terminalResultsDiv.scrollHeight;
}

function setUserResponse(message) {
  if(validate_type != "" && !hqtValidate(validate_type,message))
  {
    $('#hqttooltiptext').show().fadeIn(500);
    $('#hqttooltiptext').text('Please type a valid '+validate_type+' format!');
    $(".usrInput").focus();
    return false;
  }
  else
  {
    $('#hqttooltiptext').css('display', 'none');
  }
  const user_response = `<img class="userAvatar" src='data:image/jpeg;base64,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'><p class="userMsg">${message} </p><div class="clearfix"></div>`;
  $(user_response).appendTo(".chats").show("slow");

  $(".usrInput").val("");
  scrollToBottomOfResults();
  showBotTyping();
  //$(".suggestions").remove();
  return true;
}

function getBotResponse(text) {
  botResponse = `<img class="botAvatar" src="`+bot_avatar+`"/><span class="botMsg">${text}</span><div class="clearfix"></div>`;
  return botResponse;
}

function setBotResponse(response,message="") {
  setTimeout(() => {
    hideBotTyping();
    if (response.length < 1) {
      const fallbackMsg = "I am facing some issues, please try again later!!!";
      const BotResponse = `<img class="botAvatar" src="`+bot_avatar+`"/><p class="botMsg">${fallbackMsg}</p><div class="clearfix"></div>`;
      $(BotResponse).appendTo(".chats").hide().fadeIn(500);
      scrollToBottomOfResults();
    } else {
		console.log("Response from Rasa: ", response, "\nStatus: ", status);
      for (let i = 0; i < response.length; i += 1) {
        if (Object.hasOwnProperty.call(response[i], "text")) {
          if (response[i].text != null) {
            let botResponse;
            let html = converter.makeHtml(response[i].text);
            //console.log("Response from Rasa: ", html, "\nStatus: ", status);
            html = html
              .replaceAll("<p>", "")
              .replaceAll("</p>", "")
              .replaceAll("<strong>", "<b>")
              .replaceAll("</strong>", "</b>");
            html = html.replace(/(?:\r\n|\r|\n)/g, "<br>");
            //console.log("Response from Rasa: ", html, "\nStatus: ", status);
            // check for blockquotes
            if (html.includes("<blockquote>")) {
              html = html.replaceAll("<br>", "");
              botResponse = getBotResponse(html);
            }
            if (html.includes("<b>")) {
              //html = html.replaceAll("<br>", "");
              botResponse = getBotResponse(html);
            }
            // check for image
            if (html.includes("<img")) {
              html = html.replaceAll("<img", '<img class="imgcard_mrkdwn" ');
              botResponse = getBotResponse(html);
            }
            // check for preformatted text
            if (html.includes("<pre") || html.includes("<code>")) {
              botResponse = getBotResponse(html);
            }
            // check for list text
            if (
              html.includes("<ul") ||
              html.includes("<ol") ||
              html.includes("<li") ||
              html.includes("<h3") 
            ) 
            {
              //html = html.replaceAll("<br>", "");
              // botResponse = `<img class="botAvatar" src="./static/img/sara_avatar.png"/><span class="botMsg">${html}</span><div class="clearfix"></div>`;
              botResponse = getBotResponse(html);
            } 
            else {
              // if no markdown formatting found, render the text as it is.
              if (!botResponse) {
                botResponse = `<img class="botAvatar" src="${bot_avatar}"/><p class="botMsg">${response[i].text}</p><div class="clearfix"></div>`;
              }
            }
            // append the bot response on to the chat screen
            $(botResponse).appendTo(".chats").hide().fadeIn(500);
          }
        }
        // check if the response contains "buttons"
        if (Object.hasOwnProperty.call(response[i], "buttons")) {
          if (response[i].buttons.length > 0) {
            addSuggestion(response[i].buttons);
          }
        }
        // check if the response contains "images"
        if (Object.hasOwnProperty.call(response[i], "image")) {
          if (response[i].image !== null) {
            const BotResponse = `<div class="singleCard"><img class="imgcard" src="${response[i].image}"></div><div class="clearfix">`;

            $(BotResponse).appendTo(".chats").hide().fadeIn(500);
          }
        }
        // check if the response contains "attachment"
        if (Object.hasOwnProperty.call(response[i], "attachment")) {
          if (response[i].attachment != null) {
            if (response[i].attachment.type === "video") {
              // check if the attachment type is "video"
              const video_url = response[i].attachment.payload.src;

              const BotResponse = `<div class="video-container"> <iframe src="${video_url}" frameborder="0" allowfullscreen></iframe> </div>`;
              $(BotResponse).appendTo(".chats").hide().fadeIn(500);
            }
          }
        }
        // check if the response contains "custom" message
        if (Object.hasOwnProperty.call(response[i], "custom")) {
          if (Object.hasOwnProperty.call(response[i].custom, "validate")) 
          {
            validate_type = response[i].custom.validate;
          }
          else
          {
            validate_type = "";
          }
          
          if (Object.hasOwnProperty.call(response[i].custom, "payload")) 
          {
            custom_payload = response[i].custom.payload;
          }
          else
          {
            custom_payload = "";
          }
          if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
          {
            cache = response[i].custom.cache;
            if(cache == false)
            {
              cacheResponse= {};
            }
          }
          const { type,autodelete,allowtype } = response[i].custom;
          if (allowtype == true) {
            $("#userInput").prop("disabled", false);
          }
          else
          {
            $("#userInput").prop("disabled", true);
          }
      
          if (type === "quickReplies") {
            // check if the custom type is "quickReplies"
            const quickRepliesData = response[i].custom.data;
            showQuickReplies(quickRepliesData,autodelete);
            return;
          }
          // check if the response contains "buttons"
          if (type === "buttonList") {
            const buttonsData = response[i].custom.data;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"buttonList", "data":buttonsData};
              }
            }
            sub_text = "";
            if (Object.hasOwnProperty.call(response[i].custom, "text")) 
            {
              sub_text = response[i].custom.text;
            }
            addSuggestion(buttonsData,sub_text,autodelete);
          }
          // check if the response contains "yesnoblock"
          if (type === "yesnoblock") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            let pageRange = 3;
            if (Object.hasOwnProperty.call(response[i].custom, "pageRange")) 
            {
              pageRange = response[i].custom.pageRange
            }
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"yesnoblock", "data":blockData};
              }
            }
            addYesNoBlock(blockData,payload,pageRange);
          }
          // check if the response contains "bmiblock"
          if (type === "bmiblock") {
            const blockData = response[i].custom;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"bmiblock", "data":blockData};
              }
            }
            addBMIBlock(blockData,payload);
          }
          // check if the response contains "bodyblock"
          if (type === "bodyblock") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"bodyblock", "data":blockData};
              }
            }
            addBodyBlock(blockData,payload);
          }
          // body block for chest
          if (type === "bodyblockchest") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"bodyblockchest", "data":blockData};
              }
            }
            addBodyBlockChest(blockData,payload);
          }

          // body block for Joint
          if (type === "bodyblockjoint") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"bodyblockjoint", "data":blockData};
              }
            }
            addBodyBlockJoint(blockData,payload);
          }

          // body block for Joint hand img1
          if (type === "bodyblockjointHandimage1") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"bodyblockjointHandimage1", "data":blockData};
              }
            }
            addBodyBlockjoint_Hand_image1(blockData,payload);
          }

            // body block for Joint hand img1 part2
          if (type === "bodyblockjointHandimage1_part2") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"bodyblockjointHandimage1_part2", "data":blockData};
              }
            }
            addBodyBlockjoint_Hand_image1_part2(blockData,payload);
          }

           // body block for Joint hand img1 part3
           if (type === "bodyblockjointHandimage1_part3") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"bodyblockjointHandimage1_part3", "data":blockData};
              }
            }
            addBodyBlockjoint_Hand_image1_part3(blockData,payload);
          }





           // body block for Joint hand img2
          if (type === "bodyblockjointHandimage2") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"bodyblockjointHandimage2", "data":blockData};
              }
            }
            addBodyBlockjoint_Hand_image2(blockData,payload);
          }

           // body block for Joint hand img3
          if (type === "bodyblockjointHandimage3") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"bodyblockjointHandimage3", "data":blockData};
              }
            }
            addBodyBlockjoint_Hand_image3(blockData,payload);
          }

            // body block for symptoms on body
          if (type === "bodyblockSymptomsOnBody") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"bodyblockSymptomsOnBody", "data":blockData};
              }
            }
            addBodyBlockSymptomsOnBody(blockData,payload);
          }

             // body block for symptoms on body1
          if (type === "bodyblockSymptomsOnBody1") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"bodyblockSymptomsOnBody1", "data":blockData};
              }
            }
            addBodyBlockSymptomsOnBody1(blockData,payload);
          }


          // body block for back pain
          if (type === "bodyblockbackpain") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"bodyblockbackpain", "data":blockData};
              }
            }
            addBodyBlockBackpain(blockData,payload);
          }


          if (type === "userdata") {
            const payload = response[i].custom.payload;
            adduserdataBlock(payload);
          }

          // check if the response contains "userinfo"

          if (type === "userinfo") {
            const payload = response[i].custom.payload;
            addUserInfoBlock(payload);
          }
          // check if the response contains "Feedback"
          if (type === "feedback") {
            const blockData = response[i].custom.data;
            const listDate = response[i].custom.date;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"feedback", "data":blockData};
              }
            }
            addFeedBack(blockData,listDate,payload);
          }
          // check if the response contains "calendarbox"
          if (type === "calendarbox") {
            const payload = response[i].custom.payload;
            const entity = response[i].custom.entity;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"calendarbox", "data":blockData};
              }
            }
            addCalendarBox(payload,entity);
          }
          // check if the response contains "datebox"
          if (type === "datebox") {
            const blockData = response[i].custom;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"datebox", "data":blockData};
              }
            }
            addDateBox(blockData);
          }
          // check if the response contains "timebox"
          if (type === "timebox") {
            const blockData = response[i].custom;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"timebox", "data":blockData};
              }
            }
            addTimeBox(blockData);
          }
          // check if the response contains "uploadImageBox"
          if (type === "uploadImageBox") {
            var checktype = response[i].custom.checktype
            var url = "http://46.51.221.113:8001/api/uploadImage"
            if (Object.hasOwnProperty.call(response[i].custom, "url")) 
            {
             url = response[i].custom.url
            }
            addUploadImageBox(checktype,url);
          }
          // check if the response contains "durationquestion"
          if (type === "durationQuestionBox") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"durationQuestionBox", "data":blockData};
              }
            }
            addDurationQuestionBox(blockData,payload);
          }
          // check if the response contains "faceblock"
          if (type === "faceblock") {
            const blockData = response[i].custom.data;
            const payload = response[i].custom.payload;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"durationQuestionBox", "data":blockData};
              }
            }
            addFaceBlock(blockData,payload);
          }
          // check if the custom type is "pdf_attachment"
          if (type === "pdf_attachment") {
            renderPdfAttachment(response[i]);
            return;
          }
		  
          if (type === "openlink") {
            window.open(dropDownData = response[i].custom.data, '_blank');
            return;
          }

          // check if the custom type is "dropDown"
          if (type === "dropDown") {
            const dropDownData = response[i].custom.data;
            renderDropDwon(dropDownData);
            return;
          }

          // check if the custom type is "cardsCarousel"
          if (type === "cardsCarousel") {
            const cardsCarouselData = response[i].custom.data;
            if (Object.hasOwnProperty.call(response[i].custom, "cache")) 
            {
              cache = response[i].custom.cache
              if(cache == true)
              {
                cacheResponse[message] = {"type":"cardsCarousel", "data":cardsCarouselData};
              }
            }
            showCardsCarousel(cardsCarouselData);
            //return;
          }
          // check of the custom payload type is "collapsible"
          if (type === "collapsible") {
            const { data } = response[i].custom;
            // pass the data variable to createCollapsible function
            createCollapsible(data);
          }
        }
        else
        {
          validate_type = "";
        }
      }
      scrollToBottomOfResults();
    }
    $(".usrInput").focus();
  }, 100);
}

async function send(message) {
	if(message == "backhistory" && historyAction.length > 0)
	{
		if(firstBack) 
		{
			historyAction.pop();
			firstBack = false;
		}
		message = historyAction.pop();
	}
	else
	{
		if(message == "backhistory")
		{
			message = initAction;
		}
		else historyAction.push(message);
		firstBack = true;
	}
	
	scrollToBottomOfResults();
	if(cacheResponse[message] != undefined)
	{
	   if(cacheResponse[message]['type'] == "cardsCarousel")
	   {
			showCardsCarousel(cacheResponse[message]["data"]);
	   }
	   else if(cacheResponse[message]['type'] == "buttonList")
	   {
		   addSuggestion(cacheResponse[message]["data"]);
	   }
     else if(cacheResponse[message]['type'] == "bodyblock")
	   {
		   addBodyBlock(cacheResponse[message]["data"]);
	   }
     else if(cacheResponse[message]['type'] == "calendarbox")
	   {
		   addCalendarBox(cacheResponse[message]["data"]);
	   }
     else if(cacheResponse[message]['type'] == "datebox")
	   {
		   addDateBox(cacheResponse[message]["data"]);
	   }
	   scrollToBottomOfResults();
	   hideBotTyping();
	   return;
	}

	await new Promise((r) => setTimeout(r, 500));
	$.ajax({
		url: rasa_server_url,
		type: "POST",
		contentType: "application/json",
		data: JSON.stringify({ message, sender: sender_id }),
		success(botResponse, status) {
			//console.log("Response from Rasa: ", botResponse, "\nStatus: ", status);
			if (message.toLowerCase().includes(initAction) && use_livechat != "") {
				$("#userInput").prop("disabled", true);
			//return;
			}
			if (use_livechat != "" && message.toLowerCase().includes(use_livechat)) {
				$("#userInput").prop("disabled", false);
				$("#userInput").focus();
			}
			
			setBotResponse(botResponse,message);

      if(use_session) sessionStorage.setItem('cache_chats', $("#chats").html());
		},
		error(xhr, textStatus) {
			if (message.toLowerCase() === initAction) {
			$("#userInput").prop("disabled", true);
			}
			setBotResponse("","");
			console.log("Error from bot end: ", textStatus);
		}
	});
}

function hqtValidate(type,value) {
  pattern = "";
  if (type == 'email')
  {
    pattern = /^(?=.{1,81}$)[\w\.-]+@[\w\.-]+\.\w{2,4}$/;
  }
  if (type == 'time')
  {
    pattern = /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/;
  }
  if (type == 'date')
  {
    pattern = /^(0?[1-9]|1[0-2])[\/](0?[1-9]|[12]\d|3[01])[\/](19|20)\d{2}$/;
  }
  if (type == 'phone')
  {
    pattern = /^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$/;
  }
  if (type == 'otp')
  {
    pattern = /^\d{6,6}$/;
  }
  if(pattern == "") return true;
  return pattern.test(value);
}

function restartConversation() {
  $("#userInput").prop("disabled", true);
  cacheResponse = {}
  $(".chats").html("");
  $("#usrInput").val("");
  send("/wellcome");
}
/// END CHAT

$(document).on("click", ".collapsible-menu-content-list-item", function () {
	$(".chart-container").remove();
	for (const item of chatChart) { // You can use `let` instead of `const` if you like
		item.destroy();
	}
	const payload = this.getAttribute("data-payload");
	const text = this.innerText;
	setUserResponse(text);
	send(payload);
	$("#userInput").prop('disabled', false);
	$("#collapsible-menu-content").hide();
});

// Global var
firstBack = true;
validate_type = ""
custom_payload = ""
clicked = false;
///
delayInMilliseconds = 30000

window.addEventListener('load', () => {
  // initialization
  $(document).ready(() => {
    
    $(document.body).append(webchat_container);
    // Toggle the chatbot screen
    
  
    
    $("#profile_div").click(() => {
      clicked = true;
      $(".profile_div").toggle();
      $(".hqtwidget").toggle();
    });
    

      setTimeout(function() {

        $("#profile_div").ready(() => {
        if (clicked != true){

          $(".profile_div").toggle();
          $(".hqtwidget").toggle();
      }

        });
      }, delayInMilliseconds);
    
    
    // clear function to clear the chat contents of the hqtwidget.
    $("#clear").click(() => {
    $(".chats").fadeOut("normal", () => {
      $(".chats").html("");
      $(".chats").fadeIn();
    });
    });
    // close function to close the hqtwidget.
    $("#close").click(() => {
      $(".profile_div").toggle();
      $(".hqtwidget").toggle();
      scrollToBottomOfResults();
    });
    // triggers restartConversation function.
    $("#restart").click(() => {
      restartConversation();
    });
    $("#maximize").click(() => {
      $(".hqtwidget").css('height',window.innerHeight);
      $(".hqtwidget").css('width',window.innerWidth);
      $(".chats").css('height',window.innerHeight - 120);
      $(".hqtwidget").css('bottom',0);
      $(".hqtwidget").css('right',1);
      $("#normal").show();
      $("#maximize").hide();
      scrollToBottomOfResults();
    });
      
    $("#normal").click(() => {
      $(".hqtwidget").css('height',window.innerHeight*80/100);
      $(".hqtwidget").css('width',webchat_width);
      $(".chats").css('height',window.innerHeight*80/100 - 120);
      $(".hqtwidget").css('bottom','5%');
      $(".hqtwidget").css('right','15px');
      //$(".chats").css('height',$(window).height()*76/100);
      $("#maximize").show();
      $("#normal").hide();
      scrollToBottomOfResults();
    });
    
    $( window ).resize(function() {
      $(".hqtwidget").css('height',window.innerHeight*webchat_height/100);
      $(".chats").css('height',window.innerHeight*80/100 - 120);
    });
    
    $("#collapsible-menu").click(() => {
      if ($("#collapsible-menu-content").is(":hidden")) {
        $("#collapsible-menu-content").show();	
        $("#collapsible-menu-icon").css('transform','rotate(180deg)');	
      } else {
        $("#collapsible-menu-content").hide();
        $("#collapsible-menu-icon").css('transform','rotate(360deg)');
      }
    });
    
    $(".usrInput").on("keyup keypress", (e) => {
      const keyCode = e.keyCode || e.which;
      const text = $(".usrInput").val();
      if(text == "")
      {
        $('#hqttooltiptext').css('display', 'none');
      }
      else if(hqtValidate(validate_type,text))
      {
        $('#hqttooltiptext').css('display', 'none');
      }
      if (keyCode === 13) {
        if (text === "" || $.trim(text) === "") {
          e.preventDefault();
          return false;
        }

        $(".usrInput").blur();
        if (!setUserResponse(text)) return;
        if(custom_payload != "")
        {
          custom_payload = custom_payload.replace("user_input",text)
          send(custom_payload);
        }
        else send(text);
        e.preventDefault();
        return false;
      }
      return true;
    });

    $("#sendButton").on("click", (e) => {
      const text = $(".usrInput").val();
      if(text == "")
      {
        $('#hqttooltiptext').css('display', 'none');
      }
      else if(hqtValidate(validate_type,text))
      {
        $('#hqttooltiptext').css('display', 'none');
      }
      if (text === "" || $.trim(text) === "") {
        e.preventDefault();
        return false;
      }
      $(".usrInput").blur();
      if (!setUserResponse(text)) return;
      if(custom_payload != "")
      {
        custom_payload = custom_payload.replace("user_input",text)
        send(custom_payload);
      }
      else send(text);
      
      e.preventDefault();
      return false;
    });
    
    $(".hqtdropdown-trigger").dropdown();
    $(".chat_header").css('background',header_bg_color);
    $(".chat_header").css('border-bottom',header_bg_bottom_color);
    $(".chat_header .chat-name").css('color',header_color);
    $('.chat-name').html(header_text);
    $('.hqtwidget').css('height', window.innerHeight*webchat_height/100);
    $(".chats").css('height',window.innerHeight*webchat_height/100 - 120);
    if(window.matchMedia("(max-width: 767px)").matches){
      $('.hqtwidget').css('width', window.innerWidth);
      $('.hqtwidget').css('height', window.innerHeight);
      $('.hqtwidget').css('right', '1px');
      $('.hqtwidget').css('bottom', '1px');
      $(".chats").css('height',window.innerHeight - 120);
    }
    
    $('#userInput').attr("placeholder", placeholder_text);
    if (bot_avatar_url != "" || bot_avatar_url == undefined) bot_avatar_default = bot_avatar_url;
    if (header_logo_url != "" || header_logo_url == undefined) $(".chat-logo").attr("src", header_logo_url);
    if (user_avatar_url != "" || user_avatar_url == undefined) $(".userAvatar").attr("src", user_avatar_url);
    if (bot_avatar_profile_url != "" || bot_avatar_profile_url == undefined) {$(".imgProfile").attr("src", bot_avatar_profile_url);}
    if (use_collapsible_menu != "" && use_collapsible_menu == true) {$("#collapsible-menu").show()} else {$("#collapsible-menu").hide()};
    
    //localStorage.removeItem('cache_chats');
    if(use_session && sessionStorage.getItem('cache_chats') != null)
    {
      $('#chats').html(sessionStorage.getItem('cache_chats'));
      return;
    }
      
    showBotTyping();
    if(use_livechat != "") $("#userInput").prop('disabled', true);
    send(initAction)
  });	
});

var sender_id_ = "";
if(localStorage.getItem('sender_id') == null)
{
  sender_id_ = uuidv4();
  localStorage.setItem('sender_id', sender_id_);
}
else sender_id_ = localStorage.getItem('sender_id');
url = window.location.href
var pathname = new URL(url).pathname;

console.log(pathname);
var initAction = "";

if (pathname=="/aidepression")
{
var  initAction = "/welcome_depression";
}
else if (pathname=="/aiskin")
{
var  initAction = "/welcome_skin";
}
else if (pathname=="/aianxiety")
{
var  initAction = "/welcome_anxiety";
}
else if (pathname=="/aifever")
{
var  initAction = "/welcome_fever";
}
else if (pathname=="/aicough")
{
var  initAction = "/welcome_cough";
}
else if (pathname=="/aidiabetes")
{
var  initAction = "/welcome_diabetes";
}
else if (pathname=="/aigastro")
{
var  initAction = "/welcome_gastro";
}
else if (pathname=="/aichestpain")
{
var  initAction = "/welcome_chest";
}
else if (pathname=="/aijointpain")
{
var  initAction = "/welcome_JointPain";
}
else if (pathname=="/backpain/")
{
var  initAction = "/welcome_BackPain";
}
else if (pathname=="/aibackpain")
{
var  initAction = "/welcome_BackPain";
}
else if (pathname=="/aibackpain")
{
var  initAction = "/welcome_BackPain";
}
else if (pathname=="/generaljointpain/")
{
var  initAction = "/welcome_general_jointpain";
}

else
{

  var initAction = "/wellcome";
}

///////////////////////////////////////////////////////////////////////
const defaultLanguage = "en";
const rasa_server_url = "https://bot3.apnamd.in/webhooks/rest/webhook";//"https://apnamd.medibot.com.au/webhooks/rest/webhook"; 
const sender_id = sender_id_;
const header_bg_color = "#2a73fe";
const header_color = "white";
const header_bg_bottom_color = "3px solid #2a73fe";
const header_text = "ApnaMD";
const placeholder_text = "Typing here";
const header_logo_url = "";
const bot_avatar_url = "";
const user_avatar_url = "";
const bot_avatar_profile_url = "";
const use_livechat = "";
const use_collapsible_menu = false;
const webchat_width = 480;
const webchat_height = 80; //percent
const use_session = false;
////////////////////////////////////////////////////////////////////////
$('head').append('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />');