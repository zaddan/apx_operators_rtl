#!/usr/bin/perl 
    ##################################################################
    ## Extract the original image data
    ##################################################################
    open(DATAFILE, 'gray.txt') or die "Could not open gray.txt!\n";
    $data_idx = 0;
    while(<DATAFILE>) {
    	$currentLine = $_;
    	if($currentLine =~ /^(\d+)$/) {
        $orig_data[$data_idx] = $1;
        $data_idx++;
      }
    }
    close(DATAFILE);
    ##################################################################
    ## Extract the image data after DCT and IDCT
    ##################################################################
    open(DATAFILE, "idctdata.txt") or die "Could not open idctdata.txt!\n";
    $data_idx = 0;
    while(<DATAFILE>) {
    	$currentLine = $_;
    	if($currentLine =~ /^\s*(\d+)\s*$/) {
        if($data_idx > 0) {
          $data[$data_idx - 1] = $1;
        }        
        $data_idx++;
      }
    }
    close(DATAFILE);
    $totalSize = $data_idx-1;
    $rel_err = 0;
    for($data_idx = 0; $data_idx < $totalSize ;$data_idx++) {
        	  $diff[$data_idx] = ($data[$data_idx] - $orig_data[$data_idx])*($data[$data_idx] - $orig_data[$data_idx]);
        	  $rel_err += $diff[$data_idx];
        	 # $data_idx++;
    }

    $avg_err = sqrt($rel_err/$totalSize);
    $PSNR = 20*log(255.0/$avg_err)/log(10);
    print "$PSNR\n";
