jQuery(document).ready(function ($) {
    window.selectedFeeds = [];

    $('input[name=birthday],input[name=date_founded]').datepicker({
        viewMode: 'years',
        format: 'mm/dd/yyyy'
    });

    //$container = $('.post-container');

	
    		var $container = $('.post-container');
    		var $toggleContainer = $('.toggle-post-response');
    		// initialize
    		$container.masonry({
        		//columnWidth: 200,
        		itemSelector: '.full_post',
        		"isFitWidth": true
    		});
    
    
    

    //slider menu
    new gnMenu(document.getElementById('gn-menu'));


    //tab hashtag
    /*if (location.hash !== '') {
     $('a[href="' + location.hash + '"]').tab('show');
     return;
     }
     $('a[data-toggle="tab"]').on('shown', function(e) {
     return;
     location.hash = $(e.target).attr('href').substr(1);
     });*/

    var hash = window.location.hash;
    hash && $('ul.nav a[href="' + hash + '"]').tab('show');

    jQuery('.gn-menu a').click(function () {
        //jQuery('.gn-menu-wrapper').removeClass('gn-open-all');
        //jQuery('.gn-trigger a').removeClass('gn-selected');
        //jQuery('.gn-menu-wrapper').removeClass('gn-open-part');
        var scrollmem = $('body').scrollTop();
        window.location.hash = this.hash;
        $('html,body').scrollTop(scrollmem);
        $(this).tab('show');
    });


    $('.nav-tabs a').click(function (e) {
        $(this).tab('show');
        var scrollmem = $('body').scrollTop();
        window.location.hash = this.hash;
        $('html,body').scrollTop(scrollmem);
    });

    //message center navigation
    $('.nav-tabs.nav-stacked a').click(function () {
        $('.innerNav').show();
        $('.itemListContent').hide();
        $('.innerNav li').removeClass('active')
        var tabID = $(this).attr('href');
        $(tabID).fadeIn(800);
        //see if we are clicking on a inner navigation item.
        //remove the inner nav and show the comment/post/message
        $('.innerNav a.messageLink').click(function () {
            var innertabID = $(this).attr('href');
            $('.innerNav').hide();
            $(innertabID).parent().fadeIn(800).tab('show');
        });
    });
    //compose mail
    $('.nav-tabs.nav-stacked a.firstOn').click(function () {
        $('.itemListContent').show();
        var tabID = $(this).attr('href');
        $(tabID).fadeIn(800);
    });
    //back button for the message center
    $('.itemListContent button').click(function () {
        var buttonID = $(this).find('a').attr('href');
        var buttonParent = $(this).parent();
        $(buttonParent).hide();
        $(buttonID).show();
        $(buttonID).find('ul.innerNav').show();
    });


    //carousel
    jQuery('#interestCarousel').carousel({
        interval: 5000
    });

    //search bar
    jQuery('.icon-search').click(function () {
        jQuery('.searchBar').toggle();
        $(this).toggleClass('searchBarDrop');
        $(this).toggleClass('active');
        $('.messageNotification').toggleClass('disabled');
        $('.gn-icon-menu').toggleClass('disabled');
        $('header .nav.pages').toggleClass('disabled');
    });


	//timepicker
    $('#time').timepicker({
		minuteStep: 5,
		showInputs: false
	});

    //set date for evnt
    var nowTemp = new Date();
    var now = new Date(nowTemp.getFullYear(), nowTemp.getMonth(), nowTemp.getDate(), 0, 0, 0, 0);
    var pickDate = $('.datepicker').datepicker({
        onRender: function (date) {
            return date.valueOf() < now.valueOf() ? 'disabled' : '';
        }
    });
    
    
    //toggle the comments section on the post
    jQuery('span.toggle-post-responses').click(function () {
        $(this).siblings('.post-responses').find('li:gt(1)').toggle('fast');
        $container.masonry();
        $(this).find('i').toggleClass('icon-caret-down').toggleClass('icon-caret-up');
    });

    //disable the facebook or twitter autopost when creating a post or sending a comment
    //will need to also use some django stuff to not post to social networks
    jQuery('.socialPost li i').click(function ($) {
        jQuery(this).toggleClass('disable');
    });

    //trigger the event creation box and remove the post create box
    jQuery('.gray-bottom .post-type .icon-calendar').click(function ($) {
        jQuery('#postCreate').toggle();
        jQuery('#postEvent').toggle();
        jQuery(this).toggleClass('active');
        $container.masonry();

    });

    equalheight = function (container) {

        var currentTallest = 0, currentRowStart = 0, rowDivs = new Array(), $el, topPosition = 0;

        $(container).each(function () {

            $el = $(this);
            $($el).height('auto')
            topPostion = $el.position().top;

            if (currentRowStart != topPostion) {
                for (currentDiv = 0; currentDiv < rowDivs.length; currentDiv++) {
                    rowDivs[currentDiv].height(currentTallest);
                }
                rowDivs.length = 0;
                // empty the array
                currentRowStart = topPostion;
                currentTallest = $el.height();
                rowDivs.push($el);
            } else {
                rowDivs.push($el);
                currentTallest = (currentTallest < $el.height()) ? ($el.height()) : (currentTallest);
            }
            for (currentDiv = 0; currentDiv < rowDivs.length; currentDiv++) {
                rowDivs[currentDiv].height(currentTallest);
            }
        });
    }

    $(window).load(function () {
        equalheight('.feature');
        equalheight('.media_edit .well');
        equalheight('.groups .group.well');
        $container.masonry()
    });

    $(window).resize(function () {
        equalheight('.feature');
        equalheight('.media_edit .well');
        equalheight('.groups .group.well');
        $container.masonry()

    });

    $(function () {
        $('#followAction .following').hover(function () {
            $(this).removeClass('btn-success following').addClass('btn-red unfollow');
            $(this).val("Unfollow");
        }, function () {
            $(this).removeClass('btn-red unfollow').addClass('btn-success following');
            $(this).val("Following");
        });
    });

    $('a#unblockUser').click(function () {
        $('#blockAction').submit();
        return false;
    });
    $('a#blockUser').click(function () {
        $('#blockAction').submit();
        return false;
    });
    $('a#unblockUser2').click(function () {
        $('#blockAction').submit();
        return false;
    });
    $('a#blockUser2').click(function () {
        $('#blockAction').submit();
        return false;
    });


    jQuery('.fanZone .tab-content').addClass('well');

    jQuery('.accordion').on('show hide', function (n) {
        jQuery(n.target).siblings('.accordion-heading').find('a.dataToggle i').toggleClass('icon-caret-up icon-caret-down');
    });

    $('#registerForm').submit(function (e) {
        var errors = [];
        $('#registerForm').find('input').removeClass('error');

        var valid = true;
        if (!$('input[name=first_name]').val()) {
            $('input[name=first_name]').addClass('error');
            valid = false;
            errors.push('First name is required');
        }

        var $email = $('input[name=email]');
        var filter = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        ;

        if (!$email.val()) {
            $email.addClass('error');
            valid = false;
            errors.push('Email is required');
        } else {
            if (!filter.test($email.val())) {
                valid = false;
                $email.addClass('error');
                errors.push('Email is invalid');
            }
        }

        if (!valid) {
            e.preventDefault();
            $('.error_msg').text(errors[0]);
        }
    });

    $('.loginForm').submit(function (e) {
        e.preventDefault();
        $.ajax({
            url: '/account/login/',
            method: 'POST',
            dataType: "json",
            data: $('.loginForm').serialize(),
            success: function (data) {
                if (!data['success']) {
                    $('.login_error_msg').text('invalid credentials');
                } else {
                    window.location.href = '/account/home';
                }
            }
        })
    });

    $('.icon-camera').click(function () {
        $(this).toggleClass('clicked');
    });

    function detect_location() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                var geocoder = new google.maps.Geocoder();
                var latLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);

                if (geocoder) {
                    geocoder.geocode({
                        'latLng': latLng
                    }, function (results, status) {
                        if (status == google.maps.GeocoderStatus.OK) {
                            var locationShortName = results[0].formatted_address;

                            try {
                                var components = results[0].address_components;

                                var levels = [];
                                for (var i = 0; i < components.length; i++) {
                                    if (components[i].types[0] == 'administrative_area_level_1')
                                        levels[1] = components[i].short_name

                                    if (components[i].types[0] == 'locality')
                                        levels[0] = components[i].long_name
                                }

                                locationShortName = levels.join(', ');
                            } catch (e) {
                            }

                            $('.detected-location').show().text(locationShortName);
                            $('input[name=location]').val(locationShortName);
                        } else {
                            // /console.log("Geocoding failed: " + status);
                        }
                    });
                }
            }, function () {

            });
        } else {
        }
    }

    if ($.cookie('enable-location-tracking') == "true") {
        detect_location();
        $('.icon-map-marker').addClass('clicked');
    }

    $('.icon-map-marker').click(function () {
        $(this).toggleClass('clicked');

        $.cookie('enable-location-tracking', $(this).hasClass('clicked'));

        if ($(this).hasClass('clicked')) {
            detect_location();
        } else {
            $('.detected-location').text('');
            $('input[name=location]').val('');
        }
    });


});


function vote(pk, direction) {
    var _this = this;
    $.post('/post/' + pk + '/' + direction + 'vote/', {HTTP_X_REQUESTED: 'XMLHttpRequest', 'csrfmiddlewaretoken': $($('input[name=csrfmiddlewaretoken]')[0]).val()},
        function (data) {
            if (data.success == true) {
                var likes = $('.vote-status-' + pk).find('.sidebar-total:first');
                likes.text(data.score.likes);
                likes.removeClass('single');
                if (data.score.likes < 9) {
                    likes.addClass('single');
                }

                var dislikes = $('.vote-status-' + pk).find('.sidebar-total:last')
                dislikes.text(data.score.dislikes);
                dislikes.removeClass('single');
                if (data.score.dislikes < 9) {
                    dislikes.addClass('single');
                }

            } else {
                alert('ERROR: ' + data.error_message);
            }
        }, 'json'
    )
}

$('.deactivate-account-form').submit(function (e) {
    if (confirm("Are you sure?")) {

    } else {
        e.preventDefault();
    }
})

$('.btn-close-sticky-post').click(function () {
    var $self = $(this);
    $.ajax({
        url: '/post/close/' + $(this).attr('data'),
        //data: 'application/json',
        type: 'POST',
        success: function (res) {
            if (res.success) {
                $self.closest('.full_post').hide('slow');
            }
        }
    })
});

$('input[name=show_month_day],input[name=hide_birthday]').click(function(){

    if ($('input[name=hide_birthday]').is(':checked')) {
        $('select[name=birthday_year],select[name=birthday_month],select[name=birthday_day]').hide().removeClass('required')
    } else {
        $('select[name=birthday_year],select[name=birthday_month],select[name=birthday_day]').show().addClass('required');
    }

    var show_year = !$('input[name=show_month_day]').is(':checked') && !$('input[name=hide_birthday]').is(':checked');
    $('select[name=birthday_year]').toggle(show_year);

    if (show_year) {
        $('select[name=birthday_year]').addClass('required');
    } else {
        $('select[name=birthday_year]').removeClass('required');
    }
})

$('.post-button').click(function () {
    var self = $(this);
    if (self.hasClass('disabled')) return;

    $.ajax({
        url: '/post/create/',
        data: {
            uploaded_files: JSON.stringify(uploaded_files),
            csrfmiddlewaretoken: $('#fileupload [name=csrfmiddlewaretoken]').val(),
            feed: $('[name=feed]').val(),
            location: $('[name=location]').val(),
            body: $('[name=body]').val(),
        },
        type: 'post',
        success: function (json) {
            $('html body').css('cursor', 'auto');
            if (json.success) {
                window.location.reload();
            } else {
                $('.alert').text(json.errors[0]).fadeIn(1000).delay(3000).fadeOut(1000)
            }
        },
        cache: false,
    });

});

function initDeletePostButton() {
    $('.btn-close-sticky-post').click(function () {
        var self = $(this);
        window.confirmed = false;
        window.confirm_btn = self;
        $('#dlg-delete-confirm').modal('show');
    });


    $('#dlg-delete-confirm').on('hidden', function () {
        var self = window.confirm_btn;

        if (window.confirmed) {
            $.ajax({
                url: self.attr('action'),
                type: 'post',
                success: function (data) {
                    if (data.success) {
                        var obj;

                        // We used the same approach for deleting image & post
                        if (self.hasClass('btn-remove-image')) {
                            obj = self.parent();
                        } else {
                            obj = self.closest('.full_post');
                        }

                        obj.fadeOut(500, function () {
                            self.parent().remove();
                            window.location.reload();
                        });
                    } else {
                        alert('Can not delete');
                    }
                }
            });
        }
    });
}

initDeletePostButton();

$('.btn-remove-image').click(function () {
    var self = $(this);
    window.confirmed = false;
    window.confirm_btn = self;
    $('#dlg-delete-confirm').modal('show');
});

$('.btn-remove-interest').click(function () {
    var self = $(this);

    $.ajax({
        url: self.attr('action'),
        type: 'post',
        success: function (data) {
            if (data.success) {
                var obj = self.parent();
                obj.fadeOut(500, function () {
                    self.parent().remove();
                });
            } else {
                alert('Can not delete');
            }
        }
    });
});


$('.btn-remove-follower').click(function () {
    var self = $(this);

    $.ajax({
        url: self.attr('action'),
        type: 'post',
        success: function (data) {
            if (data.success) {
                var obj = self.parent();
                obj.fadeOut(500, function () {
                    self.parent().remove();
                });
            } else {
                alert('Can not delete');
            }
        }
    });
});


$('#postForm').submit(function (e) {
    e.preventDefault();
    $("button[type=submit]").attr('disabled', 'disabled');
    $('html body').css('cursor', 'wait');

    $('#postForm [name=uploaded_files]').val(JSON.stringify(uploaded_files));

    var formData = new FormData(this);

    var form = $("#postForm");
    var data = form.serialize();
    $.ajax({
        url: form.attr('action'),
        data: formData,
        type: 'post',
        xhr: function () {// custom xhr
            myXhr = $.ajaxSettings.xhr();
            if (myXhr.upload) {// check if upload property exists
                // for handling the progress of the upload
                myXhr.upload.addEventListener('progress', function (e) {
                }, false);
            }
            return myXhr;
        },
        success: function (json) {
            $('html body').css('cursor', 'auto');
            if (json.success) {
                window.location.reload();
            } else {
                $('.alert').text(json.errors[0][1]).fadeIn(1000).delay(3000).fadeOut(1000)
            }
        },
        cache: false,
        contentType: false,
        processData: false
    });

});

$('.btn-search').click(function () {
    $('#myModal').modal();
    $('select[name=interests],select[name=similar_user]').chosen({width: '206px'});
    $('#distance_chzn .chzn-drop .chzn-search').remove();
});

$('.bio span a').click(function () {
    $('#bio').modal();
});

$('.feed-type select').chosen({disable_search_threshold: 10});

$('#similar_user_chzn').click(function () {
    $(this).toggleClass('chzn-active chzn-with-drop');
})

$("#similar_user_chzn input, #similar_user_chzn .chzn-results li").click(function (event) {
    event.stopPropagation();
});

$("#similar_user_chzn .chzn-results li").click(function (event) {
    event.stopPropagation();
    $(this).text()
});

$('input[name=similar_user_input]').focus(function () {
    $(this).siblings('ul').show()
}).blur(function () {
    $(this).siblings('ul').hide()
})

$('.login-button').click(function () {
    $('.modal.in').modal('hide')
    $('#loginModal').modal();
})

$('.signup-button').click(function () {
    $('.modal.in').modal('hide')
    $('#signUp1Modal').modal();
})

var signup_type = 'business';

function validate_signup_21() {
    var ret = true;
    $('#signup21Modal form .' + signup_type  + ' .required').each(function(){
        if ($(this).val() == '' || $(this).val() == '0' ) {
            $(this).closest('.control-group').addClass('error');
            ret = false;
        } else {
            $(this).closest('.control-group').removeClass('error');
        }
    })

    return ret;
}

$('.signup-21-button').click(function(){
    $('.modal.in').modal('hide');
    $('#signup21Modal').modal();
})

$('.signup-20-button').click(function(){
    $('.modal.in').modal('hide');
    $('#signup20Modal').modal();
})


$('.signup-4-button').click(function(){
    $('.modal.in').modal('hide');
    $('#signup4Modal').modal();
})

$('.signup-21-button').click(function () {
    $('.modal.in').modal('hide')
    $('#signup21Modal').modal();
})

function initStep5(){
    $('.modal.in').modal('hide');
    $('#signup5Modal').modal();

    if ($('#signup5Modal .modal-body').html().length > 0) return;

    $.ajax({
        url: '/registration/update_interests?step=5',
        type: 'get',
        success: function(data) {
            $('#signup5Modal .modal-body').html(data);
            $('#signup5Modal .interest').click(function(){
                $(this).toggleClass('checked');
                var interest_id = $(this).attr('interest_id');
                var url = $(this).hasClass('checked') ? '/account/interests/add/' : '/account/interests/remove/';
                $.ajax({
                    url: url + interest_id,
                    type: 'post',
                    success: function(data) {
                        }
                })
            })
            initFanZoneCarousel();

        }
    })
}

function initStep6(){
    $('.modal.in').modal('hide');
    $('#signup6Modal').modal();

    if ($('#signup6Modal .modal-body').html().length > 0) return;

    $.ajax({
        url: '/registration/update_interests?step=6',
        type: 'get',
        success: function(data) {
            $('#signup6Modal .modal-body').html(data);
            $('#signup6Modal .interest').click(function(){
                $(this).toggleClass('checked');
                var interest_id = $(this).attr('interest_id');
                var url = $(this).hasClass('checked') ? '/account/interests/add/' : '/account/interests/remove/';
                $.ajax({
                    url: url + interest_id,
                    type: 'post',
                    success: function(data) {
                    }
                })
            })
        }
    })
}

$('.signup-6-button').click(initStep6)

$('.signup-5-button').click(initStep5);

function initStep7(){
    $('.modal.in').modal('hide');
    $('#signup7Modal').modal();

    if ($('#signup7Modal .modal-body').html().length > 0) return;

    $.ajax({
        url: '/registration/update_interests?step=7',
        type: 'get',
        success: function(data) {
            $('#signup7Modal .modal-body').html(data);
            $('#signup7Modal .interest').click(function(){
                $(this).toggleClass('checked');
                var interest_id = $(this).attr('interest_id');
                var url = $(this).hasClass('checked') ? '/account/interests/add/' : '/account/interests/remove/';
                $.ajax({
                    url: url + interest_id,
                    type: 'post',
                    success: function(data) {
                    }
                })
            })
        }
    })
}

$('.signup-7-button').click(initStep7)


function initStep8(){
    $('.modal.in').modal('hide');
    $('#signup8Modal').modal();

    $.ajax({
        url: '/registration/recommend_similar_users',
        type: 'get',
        success: function(data) {
            $('#signup8Modal .modal-body').html(data);
        }
    })

}

$('.signup-8-button').click(initStep8);

$('.signup-finish-button').click(function(){
    $('.modal.in').modal('hide');

    $.ajax({
        url: '/registration/recommend_similar_users?complete=1',
        type: 'get',
        success: function(data) {
             window.location.href = '/'
        }
    })

});

$('.loginForm').submit(function(e){
    e.preventDefault();

    var self = $(this);
    var _this = this;
    $.ajax({
        url: self.attr('action'),
        type: 'post',
        dataType: 'json',
        data: self.serialize(),
        success: function (data) {
            console.log(data);
            if (data.success) {
                var obj = self.parent();
                obj.fadeOut(500, function () {
                    self.parent().remove();
                    window.location.href = '/';
                });
            } else {
                self.find('.login_error_msg').text('Invalid username or password').hide().fadeIn(1000, function () {
                    self.find('.login_error_msg').fadeOut(3000)
                });
            }
        }
    });
    return false;
});

$('#signup21Modal form').submit(function(e){
    e.preventDefault();

    window.email = $('input[name=email]');

    if (!validate_signup_21()) {
        return false;
    }

    var self = $(this);
    var _this = this;
    $.ajax({
        url: self.attr('action'),
        type: 'post',
        dataType: 'json',
        data: self.serialize(),
        success: function (data) {
            $('.modal.in').modal('hide');
            $('#signup3Modal').modal();
        }
    });
    return false;
});

$('#signup20Modal form').submit(function(e){
    e.preventDefault();

    var self = $(this);
    var _this = this;
    $.ajax({
        url: self.attr('action'),
        type: 'post',
        dataType: 'json',
        data: self.serialize(),
        success: function (data) {
            self.find('.control-group').removeClass('error');
            if (data.success) {
                $('.modal.in').modal('hide');
                $('#signup21Modal').modal();
            } else {
                for(i=0; i < data.errors.length; i++) {
                    self.find('input[name=' + data.errors[i] + ']').closest('.control-group').addClass('error');
                }
            }
        }
    });
    return false;
});

$('#signup3Modal form').submit(function(e){
    e.preventDefault();

    var self = $(this);
    var _this = this;
    $.ajax({
        url: self.attr('action'),
        type: 'post',
        dataType: 'json',
        data: self.serialize(),
        success: function (data) {
            self.find('.control-group').removeClass('error');
            if (data.success) {
                $('.modal.in').modal('hide');
                $('#signup4Modal').modal();
            } else {
                for(i=0; i < data.errors.length; i++) {
                    self.find('input[name=' + data.errors[i] + ']').closest('.control-group').addClass('error');
                }
            }
        }
    });
    return false;
});


$('#signup4Modal form').submit(function(e){
    e.preventDefault();

    var self = $(this);
    var _this = this;
    $.ajax({
        url: self.attr('action'),
        type: 'post',
        dataType: 'json',
        data: self.serialize(),
        success: function (data) {
            self.find('.control-group').removeClass('error');
            if (data.success) {
                initStep5();
            } else {
                for(i=0; i < data.errors.length; i++) {
                    self.find('input[name=' + data.errors[i] + ']').closest('.control-group').addClass('error');
                }
            }
        }
    });
    return false;
});


$('.create-event-form').submit(function (e) {
    e.preventDefault();

    var self = $(this);
    var _this = this;
    $.ajax({
        url: self.attr('action'),
        type: 'post',
        dataType: 'json',
        data: self.serialize(),
        success: function (data) {
            self.find('.control-group').removeClass('error');
            if (data.success) {
                $('.modal.in').modal('hide');
            } else {
                for(i=0; i < data.errors.length; i++) {
                    self.find('input[name=' + data.errors[i] + '],textarea[name=' + data.errors[i] + '],select[name=' + data.errors[i] + ']' ).closest('.control-group').addClass('error');
                }
            }
        }
    });
    return false;
});

$('#id_acct_type_0').click(function () {
    $('.business').hide();
    $('.individual').show();
    signup_type = 'individual';
})

$('#id_acct_type_1').click(function () {
    $('.individual').hide();
    $('.business').show();
    signup_type = 'business';
})

$('.individual').hide();

function popupwindow(url, title, w, h) {
  var left = (screen.width/2)-(w/2);
  var top = (screen.height/2)-(h/2);
  return window.open(url, title, 'toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=no, resizable=no, copyhistory=no, width='+w+', height='+h+', top='+top+', left='+left);
}

var app_model = {
    'signing_up_with_facebook': false
}

function show_signup21() {
    $('.modal.in').modal('hide');
    $('#signup21Modal').modal();
}

// Prevent closing dialog by pressing escape or click on the outside region
$('.modal').modal({
    backdrop: 'static',
    keyboard: true
})

$('.menu-item.bio').click(function(){
   $('#bioModal').modal();
});

$('.modal.in').modal('hide')


function initInterestScoller() {
    // Profile interest scroller
    var delta = $('.interest-block').width();
    window.currentScrollX = 0;
    container_with = $('.slide-container').width();
    maxOffset = $('.profile-interest-slides .interest-block').length * delta;
    if (maxOffset > container_with)
        maxOffset -= container_with;


    $('.profile-interest-slides .left-arrow').click(function(){

        if (window.currentScrollX >= delta) {
            window.currentScrollX = window.currentScrollX - delta;
        }

        $('.slide-container').animate({scrollLeft: (window.currentScrollX)}, 800)
    })

    $('.profile-interest-slides .right-arrow').click(function(){
        if ((window.currentScrollX + delta) <= maxOffset) {
            window.currentScrollX = window.currentScrollX + delta;
        }
        $('.slide-container').animate({scrollLeft: window.currentScrollX}, 800)
    })
}

function initFanZoneCarousel() {
    $('.gameZoneInterestCarousel .carousel-control.right, .gameZoneInterestCarousel .carousel-control.left').click(function(){
        var active_item = $(this).siblings('.carousel-inner').find('.item.active');
        active_item.removeClass('active');
        var next = active_item.next();
        if (next.length == 0) {
            next = $(this).siblings('.carousel-inner').find('.item:first');
        }

        next.addClass('active');
    });
}

initInterestScoller();

if (typeof(current_registration_step) != 'undefined') {
    if (current_registration_step == '2') {
        $('#signup21Modal').modal();
    } else if (current_registration_step == '3') {
        $('#signup3Modal').modal();
    } else if (current_registration_step == '4') {
        $('#signup4Modal').modal();
    } else if (current_registration_step == '5') {
        initStep5();
    } else if (current_registration_step == '6') {
        initStep6();
    } else if (current_registration_step == '7') {
        initStep7();
    } else if (current_registration_step == '8'){
        initStep8()
    }
}

function followFormSubmit(button, url) {
    $.ajax({
        url: url,
        method: 'POST',
        dataType: "json",
        data: $(button).closest('form').serialize(),
        success: function (result) {
            if (result.success) {
                $(button).val($(button).val() == 'Follow' ? 'Following' : 'Follow');
            }
        }
    })
}

$('.join-event-btn').click(function(){
    var btn = $(this);
    $.ajax({
        url: $(this).attr('link'),
        method: 'POST',
        dataType: "json",
        success: function (result) {
            if (result.success) {
                btn.text('Joined');
            }
        }
    })
})

$('.feed-stateful-button').click(function(e){
    if (!window.feed_type) {
        return;
    }

    e.preventDefault();
    $(this).toggleClass('selected');

    window.selectedFeeds = [];

    $('.feed-stateful-button.selected').each(function(){
        window.selectedFeeds.push($(this).attr('feed_type'));
    })

    //$('.post-container').masonry('destroy')
    $('.post-container').find('.full_post').not('.post_box').remove();

    $.ajax({
        url: '/post/',
        data: {
            lt: 999999,
            feed: selectedFeeds.join(',')
        },
        success: function (data) {
            data = $(data);
            for(var i=0; i< data.length;i++) {
                var elem = $(data[i]);
                $('.post-container').masonry().append( elem ).masonry( 'appended', elem );
            }

            initDeletePostButton();
            processing = false;
            $('.waiting_icon').fadeOut();
        },
        error: function (data) {
            processing = false;
            $('.waiting_icon').fadeOut();
        }
    });
})