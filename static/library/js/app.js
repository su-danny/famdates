/*all the custom jquery for the application*/

jQuery(document).ready(function($){
	
	//let's set the login and signup form to always center in the window
	//make it load on doc ready and to resize on document resize
	function formResizer() {
		windowWidth = $(window).width(); 
		marginForm = (windowWidth - ($('#formContainer').width()))*.5;
		jQuery('#formContainer').css('left', marginForm);
	}
	
	jQuery(window).resize(function() {
    		formResizer();
	});

	jQuery(document).ready(function() {
    		formResizer();
	});
	
	//toggle the login and signup forms
	jQuery('.navbar-wrapper a.signup').click(function(){
		jQuery('#loginForm').hide();
		jQuery('#signUpForm').slideToggle();
		
	});
	jQuery('.navbar-wrapper a.login').click(function(){
		jQuery('#signUpForm').hide();
		jQuery('#loginForm').slideToggle();
		
	});

	//ratings
	jQuery('#rating').on('starrr:change', function(e, value){
    		jQuery('#count').html(value);
  	});
  	
  	var hash = window.location.hash;
  	hash && $('ul.nav a[href="' + hash + '"]').tab('show');
  	
  	jQuery('.nav-tabs a').click(function (e) {
    		jQuery(this).tab('show');
    		var scrollmem = jQuery('body').scrollTop();
    		window.location.hash = this.hash;
    		jQuery('html,body').scrollTop(scrollmem);
  	});
  
  	//message center
	jQuery('#message-center .nav-tabs.nav-stacked a').click(function(){
		jQuery('.innerNav').show();
		jQuery('.itemListContent').hide();
		jQuery('.innerNav li').removeClass('active')
		var tabID = jQuery(this).attr('href');
		jQuery(tabID).fadeIn(800);
		//see if we are clicking on a inner navigation item. 
		//remove the inner nav and show the comment/post/message
		jQuery('.innerNav a.messageLink').click(function() {
			var innertabID = jQuery(this).attr('href');
			jQuery(this).parent().removeClass('unreadMessage');
			jQuery(this).parent().find('.messageActions .fa-check').show();
			//use this to show that a message has been replied to
			jQuery(this).parent().find('.messageActions .fa-mail-reply').show();
			jQuery('.innerNav').hide();
			jQuery(innertabID).parent().fadeIn(800).tab('show');
		});
		
	});
	//compose mail
	jQuery('#message-center .nav-tabs.nav-stacked a.firstOn').click(function(){
		jQuery('.itemListContent').show();
		var tabID = jQuery(this).attr('href');
		jQuery(tabID).fadeIn(800);
	});
	//back button for the message center
	jQuery('.itemListContent button').click(function(){
		var buttonID = jQuery(this).find('a').attr('href');
		var buttonDiv = jQuery(this).parent().attr('id');
		var buttonParent = jQuery(this).parent();
		jQuery(buttonParent).hide();
		jQuery(buttonID).show();
		
		jQuery(buttonID).find('ul.innerNav').show();
		
	});

	
	//graph
//	jQuery(function() {
//    		jQuery(".profileProgress").knob({
//    			angleOffset: -90,
//    			angleArc: 180,
//    			readOnly: true,
//    			bgColor: '#eff107',
//    			fgColor: '#54b3cf',
//    			width: 140,
//    			step: 5
//    		});
//
//	});
	
	//clearfix for the family profile
	jQuery('.profile.med.left.family:nth-child(3n-2)').after('<div class="clearfix"></div>');	
	
	//open the addFriend minimodal
	jQuery('.miniModal .openModal').click(function($){
		jQuery('.addFriendModal').toggle();
	});
	
//thats all folks
});