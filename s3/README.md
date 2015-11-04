#S3 Lambdas

Lambdas related to S3

##presigned_url

If you are using API Gateway you will need to set up a mapping to provide the authorization header to the lambda.

{
"authorization": "$input.params('Authorization')"
}
