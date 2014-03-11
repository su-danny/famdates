(function () {
    var e = this;
    this.Stripe = function () {
        function e() {
        }

        return e.version = 2, e.endpoint = "https://api.stripe.com/v1", e.validateCardNumber = function (t) {
            return t = (t + "").replace(/\s+|-/g, ""), t.length >= 10 && t.length <= 16 && e.luhnCheck(t)
        }, e.validateCVC = function (t) {
            return t = e.trim(t), /^\d+$/.test(t) && t.length >= 3 && t.length <= 4
        }, e.validateExpiry = function (t, n) {
            var r, i;
            return t = e.trim(t), n = e.trim(n), /^\d+$/.test(t) ? /^\d+$/.test(n) ? parseInt(t, 10) <= 12 ? (i = new Date(n, t), r = new Date, i.setMonth(i.getMonth() - 1), i.setMonth(i.getMonth() + 1, 1), i > r) : !1 : !1 : !1
        }, e.cardType = function (t) {
            return e.cardTypes[t.slice(0, 2)] || "Unknown"
        }, e.setPublishableKey = function (t) {
            e.key = t
        }, e.createToken = function (t, n, r) {
            var i, s, o;
            n == null && (n = {});
            if (!t)throw"card required";
            if (typeof t != "object")throw"card invalid";
            typeof n == "function" ? (r = n, n = {}) : typeof n != "object" && (i = parseInt(n, 10), n = {}, i > 0 && (n.amount = i));
            for (s in t)o = t[s], delete t[s], t[e.underscore(s)] = o;
            return n.card = t, n.key || (n.key = e.key || e.publishableKey), e.validateKey(n.key), e.ajaxJSONP({url: "" + e.endpoint + "/tokens", data: n, method: "POST", success: function (e, t) {
                return typeof r == "function" ? r(t, e) : void 0
            }, complete: e.complete(r), timeout: 4e4})
        }, e.getToken = function (t, n) {
            if (!t)throw"token required";
            return e.validateKey(e.key), e.ajaxJSONP({url: "" + e.endpoint + "/tokens/" + t, data: {key: e.key}, success: function (e, t) {
                return typeof n == "function" ? n(t, e) : void 0
            }, complete: e.complete(n), timeout: 4e4})
        }, e.complete = function (e) {
            return function (t, n, r) {
                if (t !== "success")return typeof e == "function" ? e(500, {error: {code: t, type: t, message: "An unexpected error has occured.\nWe have been notified of the problem."}}) : void 0
            }
        }, e.validateKey = function (e) {
            if (!e || typeof e != "string")throw new Error("You did not set a valid publishable key.\nCall Stripe.setPublishableKey() with your publishable key.\nFor more info, see https://stripe.com/docs/stripe.js");
            if (/^sk_/.test(e))throw new Error("You are using a secret key with Stripe.js, instead of the publishable one.\nFor more info, see https://stripe.com/docs/stripe.js")
        }, e
    }.call(this), typeof module != "undefined" && module !== null && (module.exports = this.Stripe), typeof define == "function" && define("stripe", [], function () {
        return e.Stripe
    })
}).call(this), function () {
    var e, t, n, r = [].slice;
    e = encodeURIComponent, t = (new Date).getTime(), n = function (t, r, i) {
        var s, o;
        r == null && (r = []);
        for (s in t)o = t[s], i && (s = "" + i + "[" + s + "]"), typeof o == "object" ? n(o, r, s) : r.push("" + s + "=" + e(o));
        return r.join("&").replace(/%20/g, "+")
    }, this.Stripe.ajaxJSONP = function (e) {
        var i, s, o, u, a, f;
        return e == null && (e = {}), o = "sjsonp" + ++t, a = document.createElement("script"), s = null, i = function () {
            var t;
            return(t = a.parentNode) != null && t.removeChild(a), o in window && (window[o] = function () {
            }), typeof e.complete == "function" ? e.complete("abort", f, e) : void 0
        }, f = {abort: i}, a.onerror = function () {
            return f.abort(), typeof e.error == "function" ? e.error(f, e) : void 0
        }, window[o] = function () {
            var t;
            t = 1 <= arguments.length ? r.call(arguments, 0) : [], clearTimeout(s), a.parentNode.removeChild(a);
            try {
                delete window[o]
            } catch (n) {
                window[o] = void 0
            }
            return typeof e.success == "function" && e.success.apply(e, t), typeof e.complete == "function" ? e.complete("success", f, e) : void 0
        }, e.data || (e.data = {}), e.data.callback = o, e.method && (e.data._method = e.method), a.src = e.url + "?" + n(e.data), u = document.getElementsByTagName("head")[0], u.appendChild(a), e.timeout > 0 && (s = setTimeout(function () {
            return f.abort(), typeof e.complete == "function" ? e.complete("timeout", f, e) : void 0
        }, e.timeout)), f
    }
}.call(this), function () {
    this.Stripe.trim = function (e) {
        return(e + "").replace(/^\s+|\s+$/g, "")
    }, this.Stripe.underscore = function (e) {
        return(e + "").replace(/([A-Z])/g, function (e) {
            return"_" + e.toLowerCase()
        })
    }, this.Stripe.luhnCheck = function (e) {
        var t, n, r, i, s, o;
        r = !0, i = 0, n = (e + "").split("").reverse();
        for (s = 0, o = n.length; s < o; s++) {
            t = n[s], t = parseInt(t, 10);
            if (r = !r)t *= 2;
            t > 9 && (t -= 9), i += t
        }
        return i % 10 === 0
    }, this.Stripe.cardTypes = function () {
        var e, t, n, r;
        t = {};
        for (e = n = 40; n <= 49; e = ++n)t[e] = "Visa";
        for (e = r = 50; r <= 59; e = ++r)t[e] = "MasterCard";
        return t[34] = t[37] = "American Express", t[60] = t[62] = t[64] = t[65] = "Discover", t[35] = "JCB", t[30] = t[36] = t[38] = t[39] = "Diners Club", t
    }()
}.call(this);