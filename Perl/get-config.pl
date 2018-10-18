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
my $req = HTTP::Request->new(GET => "<Your_URL>");
my $token = "<Your_Token>";
$req->header(Authorization => "Bearer $token");
my $resp = $ua->request($req);
if ($resp->is_success) {
    my $mess = $resp->decoded_content;
    print "$mess\n";
} else {
     my $code = $resp->content;
     print $code;
}
