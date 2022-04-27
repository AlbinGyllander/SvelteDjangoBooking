<script>
    import { Button} from "carbon-components-svelte";
</script>



<div class="container py-4">
    <div class="px-4 py-5 my-5 text-center">
        <h1 class="display-5 fw-bold">Your personal trainer!</h1>
        <div class="col-lg-6 mx-auto">
          <p class="lead mb-4">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>
          <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
              <Button>Primary button</Button>
              <Button kind="secondary">Secondary button</Button>
          </div>
        </div>
    </div>
    <div class="row align-items-md-stretch">
        <div class="col-md-6">
        <div class="h-100 p-5 text-white bg-dark ">
            <h2 class="mb-2">Change the background</h2>
            <p class="mb-3">Swap the background-color utility and add a `.text-*` color utility to mix up the jumbotron look. Then, mix and match with additional component themes and more.</p>
            <Button kind="tertiary">Secondary button</Button>
        </div>
        </div>
        <div class="col-md-6">
        <div class="h-100 p-5 bg-light border">
            <h2 class="mb-2">Add borders</h2>
            <p class="mb-3">Or, keep it light and add a border for some added definition to the boundaries of your content. Be sure to look under the hood at the source HTML here as we've adjusted the alignment and sizing of both column's content for equal-height.</p>
            <Button kind="tertiary">Secondary button</Button>
        </div>
        </div>
    </div>
</div>
<div class="container ">

    <div class="row ">
      <div class="col-lg-4 ">
        <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 140x140" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#777"></rect><text x="50%" y="50%" fill="#777" dy=".3em">140x140</text></svg>

        <h2>Heading</h2>
        <p>Some representative placeholder content for the three columns of text below the carousel. This is the first column.</p>
        <p><a class="btn btn-secondary" href="#">View details »</a></p>
      </div>
      <div class="col-lg-4">
        <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 140x140" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#777"></rect><text x="50%" y="50%" fill="#777" dy=".3em">140x140</text></svg>

        <h2>Heading</h2>
        <p>Another exciting bit of representative placeholder content. This time, we've moved on to the second column.</p>
        <p><a class="btn btn-secondary" href="#">View details »</a></p>
      </div>
      <div class="col-lg-4">
        <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 140x140" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#777"></rect><text x="50%" y="50%" fill="#777" dy=".3em">140x140</text></svg>

        <h2>Heading</h2>
        <p>And lastly this, the third column of representative placeholder content.</p>
        <p><a class="btn btn-secondary" href="#">View details »</a></p>
      </div>
    </div>
</div>



