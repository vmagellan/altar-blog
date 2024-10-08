
curl --request POST \
     --url https://api.webflow.com/v2/collections/66e851c4384f00648b0c5860/items \
     --header 'accept: application/json' \
     --header 'authorization: Bearer b85c66f8e842252c1670ecc5ff24cf2c4237779aa395b2d8a4a07edbd4458398' \
     --header 'content-type: application/json' \
     --data '
{
  "isArchived": false,
  "isDraft": false,
  "fieldData": {
    "post-summary":"just my test",
    "body-2":"just my test for body",
    "main-image":"https://altar.io/wp-content/uploads/2023/11/cta-colors-philip-still.png",
    "thumbnail-image":"https://altar.io/wp-content/uploads/2023/11/cta-colors-philip-still.png",
    "featured":true,
    "category":"d209e59717564396f2c7a72838516fac",
    "color":"#db4b68",
    "author":"66f555e31625b76ca0e3eb32",
    "name":"my post title",
    "slug":"my-post-title"
  },
  "id": "42b720ef280c7a7a3be8cabe",
  "lastPublished": "2022-11-29T16:22:43.159Z",
  "lastUpdated": "2022-11-17T17:19:43.282Z",
  "createdOn": "2022-11-17T17:11:57.148Z"
}
'