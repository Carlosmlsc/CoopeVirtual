/**
 * FastClick
 */

( function ( $ ) {
	$( function () {
        /**
         * Slidebars Controller
         */

        // Init
		var controller = new slidebars();
		controller.init();

		// Toggle main menu
		$( '.js-toggle-main-menu' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.toggle( 'main-menu' );
		} );

		// Toggle author menu
		$( '.js-toggle-author-menu' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.toggle( 'author-menu' );
		} );

		// Toggle help menu
		$( '.js-toggle-help-menu' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.toggle( 'help-menu' );
		} );

		// Toggle demo menu
		$( '.js-toggle-demos-menu' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.toggle( 'demos-menu' );
		} );

		// Close any
		$( document ).on( 'click', '.js-close-any', function ( event ) {
			if ( controller.getActiveSlidebar() ) {
				event.preventDefault();
				event.stopPropagation();
				controller.close();
			}
		} );

		// Close Slidebar links
		$( '[off-canvas] a' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();

			var url = $( this ).attr( 'href' ),
			target = $( this ).attr( 'target' ) ? $( this ).attr( 'target' ) : '_self';

			controller.close( function () {
				window.open( url, target );
			} );
		} );

		// Add close class to canvas container when Slidebar is opened
		$( controller.events ).on( 'opening', function ( event ) {
			$( '[canvas]' ).addClass( 'js-close-any' );
		} );

		// Add close class to canvas container when Slidebar is opened
		$( controller.events ).on( 'closing', function ( event ) {
			$( '[canvas]' ).removeClass( 'js-close-any' );
		} );


        // Mobile only
        var windowWidth,
        mobileOnly = function () {
            windowWidth = $( window ).width();

            if ( windowWidth > 600 ) {
                controller.close( 'demo-mobile-only' );
            }
        };

        mobileOnly();
        $( window ).on( 'resize', mobileOnly );

        $( '.js-open-demo-mobile-only' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();

            if ( windowWidth < 601 ) {
                controller.open( 'demo-mobile-only' );
            }
		} );

        $( '.js-toggle-demo-mobile-only' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();

            if ( windowWidth < 601 ) {
                controller.toggle( 'demo-mobile-only' );
            }
		} );

        $( '.js-close-demo-mobile-only' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.close( 'demo-mobile-only' );
		} );

        // Custom fixed width
        $( '.js-open-demo-custom-fixed-width' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.open( 'demo-custom-fixed-width' );
		} );

        $( '.js-toggle-demo-custom-fixed-width' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.toggle( 'demo-custom-fixed-width' );
		} );

        $( '.js-close-demo-custom-fixed-width' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.close( 'demo-custom-fixed-width' );
		} );

        // Custom fluid height
        $( '.js-open-demo-custom-fluid-height' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.open( 'demo-custom-fluid-height' );
		} );

        $( '.js-toggle-demo-custom-fluid-height' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.toggle( 'demo-custom-fluid-height' );
		} );

        $( '.js-close-demo-custom-fluid-height' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.close( 'demo-demo-custom-fluid-height' );
		} );

        // Custom responsive width
        $( '.js-open-demo-custom-responsive-width' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.open( 'demo-custom-responsive-width' );
		} );

        $( '.js-toggle-demo-custom-responsive-width' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.toggle( 'demo-custom-responsive-width' );
		} );

        $( '.js-close-demo-custom-responsive-width' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.close( 'demo-custom-responsive-width' );
		} );

        // Custom transition duration
        $( '.js-open-demo-custom-transition-duration' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.open( 'demo-custom-transition-duration' );
		} );

        $( '.js-toggle-demo-custom-transition-duration' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.toggle( 'demo-custom-transition-duration' );
		} );

        $( '.js-close-demo-custom-transition-duration' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.close( 'demo-custom-transition-duration' );
		} );

        // Custom transition duration 2
        $( '.js-open-demo-custom-transition-duration-2' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.open( 'demo-custom-transition-duration-2' );
		} );

        $( '.js-toggle-demo-custom-transition-duration-2' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.toggle( 'demo-custom-transition-duration-2' );
		} );

        $( '.js-close-demo-custom-transition-duration-2' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.close( 'demo-custom-transition-duration-2' );
		} );

        // Events
        $( '.js-events-init' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
            controller.init();
		} );

        $( '.js-events-exit' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
            controller.exit();
		} );

        $( '.js-events-css' ).on( 'click', function ( event ) {
            event.preventDefault();
            event.stopPropagation();
            controller.css();
        } );

        $( '.js-open-demo-events' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.open( 'demo-events' );
		} );

        $( '.js-toggle-demo-events' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.toggle( 'demo-events' );
		} );

        $( '.js-close-demo-events' ).on( 'click', function ( event ) {
			event.preventDefault();
			event.stopPropagation();
			controller.close( 'demo-events' );
		} );





	} );
} ) ( jQuery );