/*!
* jQuery JavaScript Library v1.9.1
* http://jquery.com/
*
* Includes Sizzle.js
* http://sizzlejs.com/
*
* Copyright 2005, 2012 jQuery Foundation, Inc. and other contributors
* Released under the MIT license
* http://jquery.org/license
*
* Date: 2013-2-4
*/

$('[data-toggle="tooltip"]').tooltip({
'placement': 'top'
});
$('[data-toggle="popover"]').popover({
trigger: 'hover',
'placement': 'top'
});

$('#userNameField').tooltip({
'show': true,
'placement': 'bottom',
'title': "Please remember to..."
});

$('#userNameField').tooltip('show');