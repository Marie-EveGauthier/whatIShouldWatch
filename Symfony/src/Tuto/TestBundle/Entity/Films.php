<?php

namespace Tuto\TestBundle\Entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * Films
 *
 * @ORM\Table()
 * @ORM\Entity(repositoryClass="Tuto\TestBundle\Entity\FilmsRepository")
 */
class Films
{
    /**
     * @var integer
     *
     * @ORM\Column(name="id", type="integer")
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    private $id;

    /**
     * @var string
     *
     * @ORM\Column(name="title", type="string", length=30)
     */
    private $title;

    /**
     * @var string
     *
     * @ORM\Column(name="year
     ", type="string", length=40)
     */
    private $year
    ;


    /**
     * Get id
     *
     * @return integer 
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * Set title
     *
     * @param string $title
     * @return Films
     */
    public function setTitle($title)
    {
        $this->title = $title;

        return $this;
    }

    /**
     * Get title
     *
     * @return string 
     */
    public function getTitle()
    {
        return $this->title;
    }

    /**
     * Set year
     *
     * @param year $year

     * @return Films
     */
    public function setYear
    ($year
    )
    {
        $this->year
         = $year
        ;

        return $this;
    }

    /**
     * Get year

     *
     * @return year 
     */
    public function getYear
    ()
    {
        return $this->year
        ;
    }

       /**
     * Set bechdel
     *
     * @param tinyint $year

     * @return Films
     */
    public function setBechdel
    ($bechdel
    )
    {
        $this->bechdel
         = $bechdel
        ;

        return $this;
    }

    /**
     * Get bechdel

     *
     * @return tinyint 
     */
    public function getBechdel
    ()
    {
        return $this->bechdel
        ;
    }
}

