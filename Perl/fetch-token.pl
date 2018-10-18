use strict;
use warnings;
use HTTP::Request;
use LWP::UserAgent;
use LWP::Simple;
use JSON::XS;
use Try::Tiny;

my $ua = LWP::UserAgent->new(
   ssl_opts => { verify_hostname => 0 },
);
my $req = HTTP::Request->new(POST => "<Your_URL>");
$req->header('content-type' => 'application/json');
my $post_data = '{ "username": "<Username>", "password": "<Password>" }';
$req->content($post_data);
my $resp = $ua->request($req);
if ($resp->is_success) {
    my $mess = $resp->decoded_content;
    print "$mess\n";
} else {
     my $content = $resp->content;
     print $content;
}
